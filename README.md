# Arquitectura de Big Data - Escenarios Prácticos

Este repositorio contiene el desarrollo de prácticas y escenarios aplicados de la asignatura **Arquitectura de Big Data**.

## Objetivo General

Explorar y comparar diferentes arquitecturas y frameworks de procesamiento distribuido de datos para entender su funcionamiento, casos de uso ideales y ventajas técnicas en entornos de Big Data.

## Escenarios

A lo largo del curso se desarrollan tres escenarios diferenciados, cada uno utilizando un framework distinto:

---

### Escenario 1: Procesamiento distribuido con [Ray](https://www.ray.io/)

Ray es un framework de ejecución distribuida de propósito general que permite paralelizar tareas de forma sencilla usando Python. Este escenario muestra cómo escalar tareas computacionales intensivas utilizando Ray Actors, Remote Functions y Ray Datasets.

---

### Escenario 2: Análisis paralelo con [Dask](https://dask.org/)

Dask proporciona estructuras de datos paralelas como `dask.array` y `dask.dataframe`, similares a NumPy y Pandas pero distribuidas. Este escenario muestra cómo adaptar un pipeline de análisis de datos tradicional para ejecutarse de forma eficiente sobre múltiples núcleos o nodos.

---

### Escenario 3: Procesamiento masivo con [Apache Spark](https://spark.apache.org/)

Apache Spark es uno de los motores de procesamiento distribuido más populares del ecosistema Big Data. Este escenario se centra en la carga, transformación y análisis de grandes volúmenes de datos con PySpark.
