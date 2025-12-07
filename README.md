# Proyecto Integrador V - Análisis de Producción de Cultivos Agrícolas

## Descripción del Proyecto

Este trabajo académico lleva a cabo un examen exhaustivo de los rendimientos de los cultivos, basándose en información disponible en Kaggle. La meta principal es analizar cuáles son las cosechas que ofrecen una mayor ventaja económica en relación a la producción (toneladas por hectárea) y al tiempo de cosecha (días hasta la recolección).

Se utilizan métodos de ciencia de datos, estudios estadísticos y visualización de datos para descubrir tendencias en la productividad, evaluar cómo influyen factores como la ubicación, el tipo de suelo y las condiciones climáticas, y ofrecer datos valiosos que ayuden en la toma de decisiones dentro de la agricultura.

**Dataset:** Agriculture Crop Yield (Kaggle)  
**Registros analizados:** 1,000  
**Período:** 2016-2019  
**Variables principales:** Region, Soil_Type, Crop, Days_to_Harvest, Yield_tons_per_hectare

---

## Estructura del Proyecto

### 📁 `/src/proyecto_integrador_v/`
Directorio principal con el código fuente del proyecto.

**Archivos principales:**
- **`proyecto_integrador_v.ipynb`** - Notebook Jupyter con el análisis completo:
  - Instalación de dependencias
  - Descarga y carga del dataset desde Kaggle
  - Limpieza y validación de datos
  - Enriquecimiento con campos Trial_year y Cost_Euros
  - Creación de base de datos SQLite
  - Análisis estadístico descriptivo de 5 variables relevantes
  - 10 gráficos analíticos con interpretaciones detalladas

- **`bdatos.py`** - Módulo para gestión de base de datos SQLite:
  - Clase `Bdatos` con métodos para inserción, consulta y exportación
  - Funciones: `insertar_dataframe()`, `consultar()`, `listar_tablas()`, `contar_filas()`
  - Manejo de conexiones y transacciones

- **`ingestar.py`** - Módulo para descarga y procesamiento de datasets:
  - Clase `Ingestar` con integración a Kaggle API
  - Funciones: `download_dataset_zip()`, `load_dataset_as_dataframe()`, `extract_zip_files()`
  - Limpieza automática de datos

### 📁 `/src/proyecto_integrador_v/static/`
Directorio de recursos estáticos generados durante el análisis.

#### 📁 `/static/db/`
Base de datos y exportaciones CSV.

**Contenido:**
- **`proyecto.db`** - Base de datos SQLite con tabla Cultivos (1,000 registros)
- **`export.csv`** - Exportación del dataset original sin campos enriquecidos

#### 📁 `/static/dataset/`
Datasets enriquecidos para análisis.

**Contenido:**
- **`dataset_enriquecido.csv`** - Dataset completo con campos adicionales:
  - Campos originales del dataset de Kaggle
  - `Trial_year` (fecha AAAA-MM-DD entre 2016-2019)
  - `Cost_Euros` (costo de producción entre 879-12,654 euros)
  - `Year`, `Month` (campos derivados para análisis temporal)

### 📁 `/docs/`
Documentación y recursos del proyecto (si aplicable).

### 📁 `/build/`
Archivos de construcción del paquete Python generados durante la instalación.

### 📁 `/proyecto_integrador_v.egg-info/`
Metadatos del paquete Python.

---

## Flujo de Trabajo

1. **Adquisición de datos:** Descarga automática desde Kaggle
2. **Limpieza:** Eliminación de duplicados, valores nulos y validación de tipos
3. **Enriquecimiento:** Agregación de campos Trial_year y Cost_Euros
4. **Almacenamiento:** Creación de base de datos SQLite y exportación a CSV
5. **Análisis estadístico:** Estadísticas descriptivas de 5 variables relevantes
6. **Visualización:** 10 gráficos analíticos con interpretaciones

---

## Gráficos Implementados

1. **Distribución de rendimiento** - Líneas comparativas por cultivo y año
2. **Lluvia vs rendimiento** - Análisis de correlación por cultivo
3. **Costo mensual** - Heatmap y tendencias de costos por cultivo
4. **Correlación lluvia-cultivo-región** - 4 visualizaciones integradas
5. **Tiempo de cosecha (Cultivos)** - Barras verticales por tipo de cultivo
6. **Tiempo de cosecha (Suelos)** - Barras horizontales por tipo de suelo

---

## Instalación y Ejecución

### Requisitos
```bash
pip install pandas openpyxl requests beautifulsoup4 matplotlib "kagglehub[pandas-datasets]>=0.3.8" seaborn pyarrow
```

### Ejecución
```bash
jupyter notebook src/proyecto_integrador_v/proyecto_integrador_v.ipynb
```

### Configuración de Kaggle
Configurar credenciales de Kaggle en `~/.kaggle/kaggle.json` para descarga automática del dataset.

---

## Variables Analizadas

| Variable | Descripción | Tipo |
|----------|-------------|------|
| `Region` | Región geográfica (North, South, East, West) | Categórica |
| `Soil_Type` | Tipo de suelo (Sandy, Clay, Loam, Silt, Peaty, Chalky) | Categórica |
| `Crop` | Tipo de cultivo (Wheat, Rice, Maize, Barley, Soybean, Cotton) | Categórica |
| `Days_to_Harvest` | Días desde siembra hasta cosecha | Numérica |
| `Yield_tons_per_hectare` | Rendimiento en toneladas/hectárea | Numérica |
| `Trial_year` | Fecha de prueba (2016-2019) | Fecha |
| `Cost_Euros` | Costo de producción estimado | Numérica |

---

## Autor

Proyecto Universitario - Análisis de Datos Agrícolas  
Dataset: [Agriculture Crop Yield - Kaggle](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield)
