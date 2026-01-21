# 🚀 Mini-Proyecto -> Sales ETL Pipeline & RFM Analytics

> Un pipeline de procesamiento de datos modular construido con **Python** y **Pandas**. Transforma datos crudos de ventas en reportes de valor para el negocio.

## 🎯 Objetivo del Proyecto
Este repositorio documenta mi proceso de aprendizaje avanzado en Ingeniería de Datos. El foco no fue solo "que funcione", sino hacerlo con **buenas prácticas de arquitectura de software en Data Engineering**.

**Principales hitos de aprendizaje:**
* **Modularización:** Separación de responsabilidades (Extract, Transform, Load, Analysis).
* **Git Flow:** Flujo de trabajo profesional utilizando ramas (branches) para cada feature y fix.
* **Pandas:** Limpieza profunda de datos, manejo de tipos y agregaciones complejas.
* **Lógica de Negocio:** Implementación de métricas reales como la Matriz RFM (Recency, Frequency, Monetary).

## ⚙️ Arquitectura del Pipeline

El proyecto es orquestado por `main.py` y sigue este flujo lógico:

1.  **Extract (`extract.py`):** Ingesta de datos desde CSV crudos.
2.  **Transform (`transform.py`):**
    * Normalización de fechas (formatos mixtos).
    * Limpieza de strings y corrección de tipos de datos.
    * Manejo de nulos y duplicados.
3.  **Load - Checkpoint (`load.py`):** Guardado de seguridad de los datos limpios.
4.  **Analysis (`analysis.py`):** Generación de KPIs y segmentación de clientes (RFM).
5.  **Load - Final:** Exportación de los reportes para consumo gerencial.

## 📂 Estructura del Proyecto

```text
├── data/
│   ├── raw/          # Datos de entrada (Incluye sample para testing)
│   └── output/       # Datos limpios y Reportes generados (Output)
├── notebooks/        # Área de pruebas y exploración (Jupyter)
├── src/              # Código fuente modular
│   ├── extract.py
│   ├── transform.py
│   ├── analysis.py
│   └── load.py
├── main.py           # 🚀 Orquestador
├── requirements.txt  # Dependencias
└── README.md         # Documentación del proyecto
```