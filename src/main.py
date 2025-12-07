"""
Dashboard Interactivo - Análisis de Producción de Cultivos Agrícolas
Autor: Proyecto Integrador V
Dataset: Agriculture Crop Yield (Kaggle)
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from pathlib import Path
import sys

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Cultivos Agrícolas",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Rutas relativas al proyecto
BASE_DIR = Path(__file__).resolve().parent  # /workspaces/Proyecto_integrador_V/src
PROJECT_ROOT = BASE_DIR.parent  # /workspaces/Proyecto_integrador_V
DB_PATH = BASE_DIR / "proyecto_integrador_v" / "static" / "db" / "proyecto.db"
CSV_PATH = BASE_DIR / "proyecto_integrador_v" / "static" / "dataset" / "dataset_enriquecido.csv"

@st.cache_data
def cargar_datos():
    """Carga datos desde CSV enriquecido o base de datos SQLite"""
    try:
        if CSV_PATH.exists():
            df = pd.read_csv(CSV_PATH)
            st.sidebar.success("✅ Datos cargados desde CSV enriquecido")
        elif DB_PATH.exists():
            conn = sqlite3.connect(DB_PATH)
            df = pd.read_sql_query("SELECT * FROM Cultivos", conn)
            conn.close()
            st.sidebar.success("✅ Datos cargados desde Base de Datos")
        else:
            st.error("❌ No se encontraron archivos de datos")
            return None
        
        # Convertir Trial_year a datetime si existe
        if 'Trial_year' in df.columns:
            df['Trial_year'] = pd.to_datetime(df['Trial_year'])
            df['Year'] = df['Trial_year'].dt.year
            df['Month'] = df['Trial_year'].dt.month
        
        return df
    except Exception as e:
        st.error(f"Error al cargar datos: {e}")
        return None

def mostrar_metricas_principales(df):
    """Muestra métricas clave en la parte superior"""
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            "Total Registros",
            f"{len(df):,}",
            delta="Completo"
        )
    
    with col2:
        st.metric(
            "Tipos de Cultivos",
            df['Crop'].nunique(),
            delta=f"{df['Crop'].nunique()} variedades"
        )
    
    with col3:
        st.metric(
            "Rendimiento Promedio",
            f"{df['Yield_tons_per_hectare'].mean():.2f} t/ha",
            delta=f"±{df['Yield_tons_per_hectare'].std():.2f}"
        )
    
    with col4:
        st.metric(
            "Días Promedio Cosecha",
            f"{df['Days_to_Harvest'].mean():.0f} días",
            delta=f"Rango: {df['Days_to_Harvest'].min()}-{df['Days_to_Harvest'].max()}"
        )
    
    with col5:
        if 'Cost_Euros' in df.columns:
            st.metric(
                "Costo Promedio",
                f"€{df['Cost_Euros'].mean():,.0f}",
                delta=f"€{df['Cost_Euros'].std():,.0f}"
            )

def analisis_rendimiento_cultivos(df):
    """Análisis de rendimiento por tipo de cultivo"""
    st.header("📊 Análisis de Rendimiento por Cultivo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de barras - Rendimiento promedio
        fig, ax = plt.subplots(figsize=(10, 6))
        rendimiento_promedio = df.groupby('Crop')['Yield_tons_per_hectare'].mean().sort_values(ascending=False)
        
        colors = plt.cm.viridis(range(len(rendimiento_promedio)))
        rendimiento_promedio.plot(kind='bar', ax=ax, color=colors)
        
        ax.set_title('Rendimiento Promedio por Cultivo', fontsize=14, fontweight='bold')
        ax.set_xlabel('Tipo de Cultivo', fontsize=12)
        ax.set_ylabel('Toneladas por Hectárea', fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        st.pyplot(fig)
        
        st.markdown(f"""
        **Interpretación:**
        - **Mejor rendimiento:** {rendimiento_promedio.index[0]} ({rendimiento_promedio.values[0]:.2f} t/ha)
        - **Menor rendimiento:** {rendimiento_promedio.index[-1]} ({rendimiento_promedio.values[-1]:.2f} t/ha)
        - **Diferencia:** {(rendimiento_promedio.values[0] - rendimiento_promedio.values[-1]):.2f} t/ha
        """)
    
    with col2:
        # Boxplot - Distribución de rendimientos
        fig, ax = plt.subplots(figsize=(10, 6))
        df.boxplot(column='Yield_tons_per_hectare', by='Crop', ax=ax)
        
        ax.set_title('Distribución de Rendimientos por Cultivo', fontsize=14, fontweight='bold')
        ax.set_xlabel('Tipo de Cultivo', fontsize=12)
        ax.set_ylabel('Toneladas por Hectárea', fontsize=12)
        plt.suptitle('')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        st.pyplot(fig)
        
        # Estadísticas descriptivas
        st.markdown("**Estadísticas por Cultivo:**")
        stats = df.groupby('Crop')['Yield_tons_per_hectare'].describe()[['mean', 'std', 'min', 'max']]
        st.dataframe(stats.style.format("{:.2f}"), use_container_width=True)

def analisis_temporal(df):
    """Análisis temporal de rendimientos y costos"""
    if 'Year' not in df.columns:
        st.warning("No hay datos temporales disponibles")
        return
    
    st.header("📅 Análisis Temporal")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Tendencia de rendimiento por año
        fig, ax = plt.subplots(figsize=(10, 6))
        
        for crop in df['Crop'].unique():
            data_crop = df[df['Crop'] == crop].groupby('Year')['Yield_tons_per_hectare'].mean()
            ax.plot(data_crop.index, data_crop.values, marker='o', label=crop, linewidth=2)
        
        ax.set_title('Evolución del Rendimiento por Cultivo (2016-2019)', fontsize=14, fontweight='bold')
        ax.set_xlabel('Año', fontsize=12)
        ax.set_ylabel('Rendimiento Promedio (t/ha)', fontsize=12)
        ax.legend(title='Cultivo', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(alpha=0.3)
        plt.tight_layout()
        
        st.pyplot(fig)
    
    with col2:
        if 'Cost_Euros' in df.columns:
            # Evolución de costos
            fig, ax = plt.subplots(figsize=(10, 6))
            
            costos_anuales = df.groupby('Year')['Cost_Euros'].mean()
            ax.plot(costos_anuales.index, costos_anuales.values, marker='s', 
                   color='coral', linewidth=3, markersize=10)
            
            ax.set_title('Evolución del Costo Promedio de Producción', fontsize=14, fontweight='bold')
            ax.set_xlabel('Año', fontsize=12)
            ax.set_ylabel('Costo Promedio (€)', fontsize=12)
            ax.grid(alpha=0.3)
            
            # Añadir valores
            for x, y in zip(costos_anuales.index, costos_anuales.values):
                ax.text(x, y, f'€{y:,.0f}', ha='center', va='bottom', fontsize=10)
            
            plt.tight_layout()
            st.pyplot(fig)

def analisis_regional(df):
    """Análisis por región geográfica"""
    st.header("🗺️ Análisis Regional")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Rendimiento por región
        fig, ax = plt.subplots(figsize=(10, 6))
        
        region_data = df.groupby('Region')['Yield_tons_per_hectare'].mean().sort_values(ascending=True)
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
        
        region_data.plot(kind='barh', ax=ax, color=colors)
        ax.set_title('Rendimiento Promedio por Región', fontsize=14, fontweight='bold')
        ax.set_xlabel('Toneladas por Hectárea', fontsize=12)
        ax.set_ylabel('Región', fontsize=12)
        ax.grid(axis='x', alpha=0.3)
        
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        # Heatmap - Región vs Cultivo
        fig, ax = plt.subplots(figsize=(10, 6))
        
        pivot_data = df.pivot_table(
            values='Yield_tons_per_hectare',
            index='Region',
            columns='Crop',
            aggfunc='mean'
        )
        
        sns.heatmap(pivot_data, annot=True, fmt='.2f', cmap='YlOrRd', ax=ax, cbar_kws={'label': 't/ha'})
        ax.set_title('Rendimiento por Región y Cultivo', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)

def analisis_suelo(df):
    """Análisis por tipo de suelo"""
    st.header("🌱 Análisis por Tipo de Suelo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Días hasta cosecha por tipo de suelo
        fig, ax = plt.subplots(figsize=(10, 6))
        
        soil_days = df.groupby('Soil_Type')['Days_to_Harvest'].mean().sort_values()
        colors = plt.cm.Spectral(range(len(soil_days)))
        
        soil_days.plot(kind='barh', ax=ax, color=colors)
        ax.set_title('Días Promedio hasta Cosecha por Tipo de Suelo', fontsize=14, fontweight='bold')
        ax.set_xlabel('Días', fontsize=12)
        ax.set_ylabel('Tipo de Suelo', fontsize=12)
        ax.grid(axis='x', alpha=0.3)
        
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        # Rendimiento por tipo de suelo
        fig, ax = plt.subplots(figsize=(10, 6))
        
        df.boxplot(column='Yield_tons_per_hectare', by='Soil_Type', ax=ax)
        ax.set_title('Distribución de Rendimiento por Tipo de Suelo', fontsize=14, fontweight='bold')
        ax.set_xlabel('Tipo de Suelo', fontsize=12)
        ax.set_ylabel('Toneladas por Hectárea', fontsize=12)
        plt.suptitle('')
        plt.xticks(rotation=45, ha='right')
        
        plt.tight_layout()
        st.pyplot(fig)

def explorador_datos(df):
    """Explorador interactivo de datos"""
    st.header("🔍 Explorador de Datos")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        crops = st.multiselect(
            "Selecciona Cultivos",
            options=df['Crop'].unique(),
            default=df['Crop'].unique()[:3]
        )
    
    with col2:
        regions = st.multiselect(
            "Selecciona Regiones",
            options=df['Region'].unique(),
            default=df['Region'].unique()
        )
    
    with col3:
        soils = st.multiselect(
            "Selecciona Tipos de Suelo",
            options=df['Soil_Type'].unique(),
            default=df['Soil_Type'].unique()[:3]
        )
    
    # Filtrar datos
    df_filtered = df[
        (df['Crop'].isin(crops)) &
        (df['Region'].isin(regions)) &
        (df['Soil_Type'].isin(soils))
    ]
    
    st.write(f"**Registros filtrados:** {len(df_filtered)} de {len(df)}")
    
    # Mostrar datos filtrados
    st.dataframe(df_filtered, use_container_width=True, height=400)
    
    # Descargar datos filtrados
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar Datos Filtrados (CSV)",
        data=csv,
        file_name='datos_filtrados.csv',
        mime='text/csv'
    )

def main():
    """Función principal del dashboard"""
    
    # Título principal
    st.title("🌾 Dashboard de Análisis de Cultivos Agrícolas")
    st.markdown("**Proyecto Integrador V** | Dataset: Agriculture Crop Yield (Kaggle)")
    st.markdown("---")
    
    # Cargar datos
    df = cargar_datos()
    
    if df is None:
        st.stop()
    
    # Sidebar - Navegación
    st.sidebar.title("📋 Navegación")
    st.sidebar.markdown("---")
    
    opciones = [
        "🏠 Resumen General",
        "📊 Análisis de Rendimiento",
        "📅 Análisis Temporal",
        "🗺️ Análisis Regional",
        "🌱 Análisis de Suelo",
        "🔍 Explorador de Datos"
    ]
    
    seleccion = st.sidebar.radio("Selecciona una sección:", opciones)
    
    st.sidebar.markdown("---")
    st.sidebar.info(f"""
    **Información del Dataset:**
    - Registros: {len(df):,}
    - Cultivos: {df['Crop'].nunique()}
    - Regiones: {df['Region'].nunique()}
    - Tipos de Suelo: {df['Soil_Type'].nunique()}
    """)
    
    # Mostrar sección seleccionada
    if seleccion == "🏠 Resumen General":
        mostrar_metricas_principales(df)
        st.markdown("---")
        
    
    elif seleccion == "📊 Análisis de Rendimiento":
        analisis_rendimiento_cultivos(df)
    
    elif seleccion == "📅 Análisis Temporal":
        analisis_temporal(df)
    
    elif seleccion == "🗺️ Análisis Regional":
        analisis_regional(df)
    
    elif seleccion == "🌱 Análisis de Suelo":
        analisis_suelo(df)
    
    elif seleccion == "🔗 Correlaciones":
        analisis_correlaciones(df)
    
    elif seleccion == "🔍 Explorador de Datos":
        explorador_datos(df)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p><strong>Proyecto Integrador V - Análisis de Producción de Cultivos Agrícolas</strong></p>
        <p>Dataset: <a href='https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield' target='_blank'>Agriculture Crop Yield - Kaggle</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()