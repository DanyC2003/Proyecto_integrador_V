# Proyecto Integrador V - Análisis de producción de Cultivos

## 1. Descripción del proyecto

El presente proyecto tiene como objetivo realizar un análisis profundo de los rendimientos agrícolas de distintos cultivos, usando como base un conjunto de datos público. El foco se encuentra en investigar cuáles cultivos tienden a presentar mayor rentabilidad en términos de producción (toneladas) y en relación con el tiempo requerido para su crecimiento. Como trabajo universitario, se propone aplicar técnicas de análisis de datos para determinar patrones de productividad y ayudar a la toma de decisiones en el ámbito agrícola. Se evalúan datos sobre días de crecimiento, rendimiento de cultivo, y condiciones asociadas (suelo, clima u otras variables disponi­bles) para extraer conclusiones relevantes para la optimización del uso del recurso tierra y para la selección estratégica de cultivos.

## 2. Dataset utilizado

**Fuente:** Kaggle
**Nombre:** *Agriculture Crop Yield*  
**Autor:** [@samuelotiattakorah](https://www.kaggle.com/samuelotiattakorah)  
**Enlace:** [https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield/data](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield/data)  
**Archivo principal:** `crop_yield.csv`  
**Licencia:** Según Kaggle, licencia abierta (normalmente *CC BY 4.0*).  
**Fecha de descarga:** Noviembre de 2025  

El dataset contiene información sobre

## 3. Variables relevantes
| Variable | Descripción |
|-----------|--------------|
| `Region` | La región geográfica donde se cultiva el cultivo |
| `Soil_Type` | El tipo de suelo en el que se planta el cultivo |
| `Crop` | El tipo de cultivo que se cultiva |
| `Days_to_Harvest` | El número de días que tarda la cosecha en cosecharse después de la siembra |
| `Yield_tons_per_hectare` | El rendimiento total de los cultivos producidos, medido en toneladas por hectárea |

## 4. Caso de uso y justificación

El caso de uso principal consiste en utilizar el análisis de datos para apoyar la decisión de qué cultivo elegir cuando se dispone de un recurso de tierra limitado, y se desea maximizar la producción (o la rentabilidad) en el menor tiempo posible. Esta justificación es especialmente relevante en contextos agrícolas donde los recursos (tierra, tiempo, insumos) son críticos. Mediante este proyecto, un gestor agrícola o una empresa del sector puede:

Identificar cultivos con mayor rendimiento por tonelada y menor tiempo de cultivo,

Priorizar los cultivos que ofrecen mejor relación “producción / días de crecimiento”,

Visualizar tendencias entre cultivos, regiones y condiciones de crecimiento,

Orientar estrategias de producción, inversión o diversificación de cultivos con base en datos.
Desde la perspectiva académica, este proyecto integra conocimientos de análisis de datos, visualización, y toma de decisiones en el ámbito agrícola, lo que lo hace relevante para entregar en un contexto universitario.

## 5. Flujo de datos implementado

El flujo de trabajo general implementado en este proyecto es el siguiente:

- Descarga y carga del dataset desde Kaggle al entorno de trabajo.
- Análisis comparativo de rentabilidad: cálculo de indicadores tales como toneladas producidas por día de cultivo, ranking de cultivos más eficientes, segmentación por región o tipo de cultivo si aplica.