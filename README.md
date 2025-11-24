# Proyecto Integrador V - Análisis de Producción de Cultivos Agrícolas

## 1. Descripción del proyecto

Este proyecto tiene como objetivo realizar un análisis profundo de los rendimientos agrícolas de distintos cultivos, utilizando un conjunto de datos público de Kaggle. El foco principal es investigar cuáles cultivos presentan mayor rentabilidad en términos de producción medida en toneladas por hectárea y en relación con el tiempo requerido para su crecimiento.

Como trabajo universitario, se aplican técnicas de análisis de datos, estadística descriptiva y visualización para determinar patrones de productividad y apoyar la toma de decisiones en el ámbito agrícola. Se evalúan datos sobre días de crecimiento, rendimiento de cultivos, condiciones climáticas, tipos de suelo y uso de insumos agrícolas para extraer conclusiones relevantes que permitan optimizar el uso de recursos y la selección estratégica de cultivos.

## 2. Dataset utilizado

**Fuente:** Kaggle  
**Nombre:** Agriculture Crop Yield  
**Autor:** Samuel Otiattakorah  
**Enlace:** [https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield/data](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield/data)  
**Archivo principal:** crop_yield.csv  
**Licencia:** CC BY 4.0  
**Fecha de descarga:** Noviembre de 2025  
**Registros analizados:** 1,000 registros  

El dataset contiene información sobre producción agrícola con 15 variables que incluyen características geográficas, climatológicas, tipo de suelo, prácticas agrícolas y resultados de producción.

## 3. Variables relevantes

Las cinco variables principales identificadas en el análisis son:

| Variable | Descripción | Tipo |
|----------|-------------|------|
| `Region` | Región geográfica donde se cultiva (North, South, East, West) | Categórica |
| `Soil_Type` | Tipo de suelo utilizado (Sandy, Clay, Loam, Silt, Peaty, Chalky) | Categórica |
| `Crop` | Tipo de cultivo producido (Wheat, Rice, Maize, Barley, Soybean, Cotton) | Categórica |
| `Days_to_Harvest` | Número de días desde la siembra hasta la cosecha | Numérica |
| `Yield_tons_per_hectare` | Rendimiento del cultivo en toneladas por hectárea | Numérica |

### Variables adicionales enriquecidas

El dataset fue enriquecido con dos variables adicionales para ampliar el análisis:

| Variable | Descripción | Rango |
|----------|-------------|-------|
| `Trial_year` | Fecha de prueba del cultivo en formato AAAA-MM-DD | 2016-2019 |
| `Cost_Euros` | Costo de producción estimado en euros | 879 - 12,654 |

## 4. Caso de uso y justificación

El caso de uso principal consiste en utilizar el análisis de datos para apoyar la decisión de qué cultivo elegir cuando se dispone de un recurso de tierra limitado y se desea maximizar la producción o la rentabilidad en el menor tiempo posible. Esta justificación es especialmente relevante en contextos agrícolas donde los recursos como tierra, tiempo e insumos son críticos.

### Beneficios para gestores agrícolas y empresas del sector

- Identificar cultivos con mayor rendimiento por tonelada y menor tiempo de cultivo
- Priorizar cultivos que ofrecen mejor relación entre producción y días de crecimiento
- Visualizar tendencias entre cultivos, regiones y condiciones de crecimiento
- Evaluar el impacto del tipo de suelo en el tiempo de cosecha y rendimiento
- Analizar la rentabilidad comparando costos de producción vs rendimiento
- Determinar el efecto del uso de fertilizantes en costos, duración del ciclo y productividad
- Orientar estrategias de producción, inversión o diversificación de cultivos basadas en datos

### Perspectiva académica

Este proyecto integra conocimientos de análisis de datos, estadística descriptiva, visualización de información y toma de decisiones en el ámbito agrícola, lo que lo hace relevante como trabajo universitario de ciencia de datos aplicada.

## 5. Flujo de datos implementado

El flujo de trabajo implementado en este proyecto incluye las siguientes etapas:

### 5.1 Adquisición de datos
- Descarga automática del dataset desde Kaggle utilizando la API de Kaggle
- Extracción de archivos comprimidos
- Carga del dataset en formato DataFrame de Pandas

### 5.2 Limpieza y validación de datos
- Eliminación de registros duplicados
- Eliminación de valores nulos
- Validación y conversión de tipos de datos numéricos
- Normalización de datos de texto
- Redondeo de valores numéricos a dos decimales

### 5.3 Enriquecimiento de datos
- Generación del campo Trial_year con fechas aleatorias entre 2016-2019
- Generación del campo Cost_Euros con valores aleatorios entre 879-12654 euros
- Creación de campos derivados: Year, Month para análisis temporal

### 5.4 Almacenamiento en base de datos
- Creación de base de datos SQLite (proyecto.db)
- Inserción de 1,000 registros en la tabla Cultivos
- Exportación de datos a formato CSV para análisis

### 5.5 Análisis estadístico descriptivo
- Cálculo de estadísticas generales usando la función describe()
- Análisis de distribución de las cinco variables relevantes
- Estadísticas por variables categóricas: Region, Soil_Type, Crop
- Estadísticas por variables numéricas: Days_to_Harvest, Yield_tons_per_hectare
- Análisis cruzado: rendimiento promedio por región, tipo de suelo y tipo de cultivo
- Análisis de días hasta cosecha segmentado por las variables categóricas

### 5.6 Visualización de datos

Se implementaron 9 gráficos analíticos organizados secuencialmente:

**Gráfico 1:** Distribución de rendimiento por toneladas por hectárea
- Histograma dual mostrando distribución por tipo de cultivo (top 5) y por año
- Permite identificar variabilidad según cultivo y temporalidad

**Gráfico 2:** Rendimiento promedio por tipo de cultivo y año
- Gráfico de barras agrupadas mostrando 6 cultivos principales durante 4 años (2016-2019)
- Identifica tendencias de productividad por cultivo a lo largo del tiempo

**Gráfico 4:** Relación entre precipitación y rendimiento
- Diagrama de dispersión con codificación de color por año
- Muestra correlación positiva entre lluvia y rendimiento

**Gráfico 5:** Matriz de correlación de variables numéricas
- Mapa de calor mostrando correlaciones entre 6 variables numéricas
- Identifica relaciones significativas: lluvia-rendimiento (0.76), fertilizante-rendimiento (0.44)

**Gráfico 6:** Costo promedio por año y tipo de cultivo
- Gráfico de barras agrupadas mostrando evolución de costos 2016-2019
- Permite evaluar fluctuaciones económicas por cultivo

**Gráfico 8:** Impacto del fertilizante en costo y duración del ciclo
- Comparación dual: costo promedio y días hasta cosecha con/sin fertilizante
- Análisis estadístico mostrando diferencias en rendimiento (38% de mejora)

**Gráfico 9:** Tiempo de cosecha por tipo de cultivo y tipo de suelo
- Gráfico de barras mostrando días promedio por combinación cultivo-suelo
- Identifica que suelo Sandy acelera cosecha (~103 días) vs Clay (~107 días)

**Gráfico 11:** Rendimiento vs temperatura por región
- Diagrama de dispersión por región y gráfico circular de proporción de rendimiento
- Muestra patrones regionales en la relación temperatura-productividad

**Gráfico 12:** Análisis de rentabilidad (rendimiento vs costo)
- Diagrama de dispersión mostrando relación costo-beneficio por cultivo
- Identifica cultivos más rentables en la zona superior izquierda del gráfico

**Gráfico 13:** Evolución mensual del rendimiento por año
- Gráfico de líneas mostrando estacionalidad del rendimiento
- Identifica periodos de mayor productividad que varían por año

## 6. Resultados principales del análisis

### 6.1 Estadísticas generales

**Días hasta cosecha:**
- Media: 104.44 días
- Rango: 60 - 149 días
- Desviación estándar: 26.67 días

**Rendimiento:**
- Media: 4.65 toneladas por hectárea
- Rango: -0.01 - 9.14 toneladas por hectárea
- Desviación estándar: 1.70 toneladas por hectárea

### 6.2 Cultivos más productivos

Por rendimiento promedio:
1. Rice: 4.80 ton/ha
2. Maize: 4.79 ton/ha
3. Soybean: 4.67 ton/ha
4. Wheat: 4.66 ton/ha
5. Cotton: 4.53 ton/ha
6. Barley: 4.44 ton/ha

### 6.3 Mejores condiciones de producción

**Por región:** East muestra el mayor rendimiento promedio (4.89 ton/ha)

**Por tipo de suelo:** 
- Silt: 4.94 ton/ha (mejor rendimiento)
- Sandy: 4.46 ton/ha (menor tiempo de cosecha: 102.92 días)

### 6.4 Impacto del uso de fertilizantes

El análisis demostró que el uso de fertilizantes:
- Reduce costos en 82.41 euros (-1.19%)
- Incrementa ligeramente el ciclo en 0.18 días (+0.17%)
- Aumenta el rendimiento en 1.50 ton/ha (+38.66%)

Conclusión: El fertilizante es altamente rentable, aumentando significativamente el rendimiento sin penalizar costos ni tiempo.

### 6.5 Factores más influyentes en el rendimiento

Según la matriz de correlación:
- Precipitación (Rainfall_mm): Correlación 0.76 (alta y positiva)
- Uso de fertilizante: Correlación 0.44 (moderada)
- Temperatura: Correlación 0.08 (casi inexistente)

La lluvia y la fertilización son los elementos más relevantes para predecir cambios en el rendimiento.

## 7. Estructura del proyecto

```
Proyecto_integrador_V/
├── README.md
├── setup.py
├── src/
│   └── proyecto_integrador_v/
│       ├── bdatos.py                    # Clase para manejo de base de datos SQLite
│       ├── ingestar.py                  # Clase para descarga y carga de datasets
│       ├── proyecto_integrador_v.ipynb  # Notebook principal con análisis completo
│       └── static/
│           ├── db/
│           │   ├── proyecto.db          # Base de datos SQLite
│           │   └── export.csv           # Exportación de datos originales
│           └── dataset/
│               └── dataset_enriquecido.csv  # Dataset con campos adicionales
├── docs/                                # Documentación adicional
└── build/                               # Archivos de construcción
```

## 8. Requisitos y dependencias

**Python:** 3.8 o superior

**Librerías principales:**
- pandas: Manipulación y análisis de datos
- numpy: Operaciones numéricas
- matplotlib: Visualización de gráficos
- seaborn: Visualización estadística avanzada
- kagglehub: Descarga de datasets desde Kaggle
- sqlite3: Base de datos (incluida en Python)
- openpyxl: Lectura de archivos Excel
- requests: Peticiones HTTP
- beautifulsoup4: Web scraping
- pyarrow: Lectura eficiente de archivos

## 9. Instalación y ejecución

### 9.1 Instalación de dependencias

Ejecutar en terminal:

```bash
pip install pandas openpyxl requests beautifulsoup4 matplotlib "kagglehub[pandas-datasets]>=0.3.8" seaborn pyarrow
```

### 9.2 Configuración de Kaggle API

Para descargar el dataset automáticamente:

1. Crear cuenta en Kaggle.com
2. Ir a Account Settings > API > Create New API Token
3. Descargar el archivo kaggle.json
4. Colocar kaggle.json en la ubicación apropiada según el sistema operativo

### 9.3 Ejecución del notebook

Abrir el archivo `proyecto_integrador_v.ipynb` en Jupyter Notebook o VS Code y ejecutar las celdas secuencialmente.

El notebook está organizado en secciones:
1. Instalación de dependencias
2. Importación de librerías
3. Descarga y carga del dataset
4. Limpieza y validación de datos
5. Enriquecimiento de datos
6. Creación de base de datos
7. Exportación a CSV
8. Preparación de datos para análisis
9. Análisis estadístico descriptivo
10. Visualizaciones (Gráficos 1-13)

## 10. Conclusiones

Este proyecto demuestra cómo el análisis de datos puede proporcionar información valiosa para la toma de decisiones en el sector agrícola. Los principales hallazgos indican que:

- La precipitación es el factor más determinante en el rendimiento de cultivos
- El uso de fertilizantes mejora significativamente la productividad con mínimo impacto en costos
- Rice y Maize son los cultivos más productivos en términos de rendimiento por hectárea
- El tipo de suelo influye tanto en el tiempo de cosecha como en el rendimiento final
- Las condiciones varían significativamente entre regiones, lo que sugiere la importancia de adaptar las estrategias de cultivo al contexto local

Estos resultados pueden servir como base para optimizar la selección de cultivos, planificar inversiones en insumos agrícolas y diseñar estrategias de producción más eficientes.