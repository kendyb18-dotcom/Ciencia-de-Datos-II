# U01.E01: Modelos avanzados, reducción dimensional y Green AI

## Descripción
Este repositorio contiene la implementación de un pipeline de Machine Learning utilizando Support Vector Machines (SVM) y Análisis de Componentes Principales (PCA) para la detección de enfermedades cardíacas (dataset *Heart Disease Cleveland*). 

El proyecto cumple con estrictos estándares de validación:
- Separación estratificada 60/20/20 (entrenamiento, validación, prueba) para prevenir fuga de datos.
- Preprocesamiento integrado en pipelines de `scikit-learn` (Imputación y Escalado).
- Paradigma *Green AI* aplicando reducción dimensional a 7 componentes.
- Arquitectura de software modular con extracción automática de artefactos hacia la carpeta `reports/`.

## Instrucciones de Ejecución Reproducible

1. Ubicarse en el directorio del proyecto:
   ```bash
   cd "Ciencia de DatosII/Unidad I/Ejercicio 01"