# Ejercicio 02: Ensambles, Reducción Dimensional y Green AI

**Asignatura:** INF-8239 Ciencia de Datos II
**Unidad:** 01 - Modelos avanzados, reducción dimensional y Green AI

**Repositorio oficial:** https://github.com/kendyb18-dotcom/Ciencia-de-Datos-II

Este repositorio contiene las evidencias ejecutables y defendibles del diseño, auditoría, modelado y análisis de costo computacional (Green AI) aplicados a la predicción de riesgo temprano de diabetes.

---

## 1. Instrucciones de Instalación y Ejecución

Para reproducir este proyecto en un entorno local aislado de configuraciones globales, siga estos pasos:

*   **Crear y activar el entorno virtual:**
    ```powershell
    python -m venv .venv
    .\.venv\Scripts\activate
    ```
*   **Instalar las dependencias:** Instale los paquetes declarados en el archivo de requerimientos.
    ```powershell
    pip install -r requirements.txt
    ```
*   **Descarga de datos:** El dataset se descarga de forma reproducible utilizando el script de datos.
    ```powershell
    python src/inf8239_u01/data.py
    ```
*   **Ejecución de pruebas:** Verifique el contrato de datos ejecutando las pruebas automatizadas de la carpeta `tests`.
    ```powershell
    $env:PYTHONPATH="src"
    python -m pytest -q
    ```

---

## 2. Ficha del Dataset y Diccionario de Datos

El conjunto de datos utilizado corresponde al *Early Stage Diabetes Risk Prediction Dataset* (ID: 529).

*   **Procedencia y Licencia:** Repositorio UCI Machine Learning. Disponible para uso académico.
*   **Dominio:** Salud preventiva y diagnóstico médico.
*   **Unidad de análisis:** El paciente individual.
*   **Target:** `class` (Binario: Positivo/Negativo para riesgo de diabetes).
*   **Métrica principal:** F1-Score (Macro) y Recall, dado que el error más costoso es el falso negativo (omitir un paciente en riesgo).

### Diccionario de Datos Breve
*   `Age` (Numérica): Edad del paciente en años.
*   `Gender` (Categórica): Género del paciente.
*   `Polyuria`, `Polydipsia`, `sudden weight loss`, `weakness`, etc. (Categóricas): Presencia de síntomas clínicos observados al momento de la evaluación.

---

## 3. Conclusión de Auditoría y Baseline (LAB02)

Durante la fase de exploración y auditoría, se verificó que el dataset consta de variables íntegramente disponibles al momento de la predicción, confirmando la ausencia de variables identificadoras o métricas que generen riesgo de fuga de datos. Se estableció un objetivo binario observable con dos clases y un volumen de datos compatible con el procesamiento en CPU. 

Para garantizar la reproducibilidad y evitar el filtrado de información entre las fases de entrenamiento y prueba, el preprocesamiento fue encapsulado estrictamente dentro de un `Pipeline` de `scikit-learn`. Las características numéricas, como la edad, fueron tratadas con un `SimpleImputer` (estrategia de la mediana) y escaladas mediante `StandardScaler`. Las características categóricas (síntomas clínicos) recibieron imputación por moda y fueron codificadas a través de un `OneHotEncoder` configurado para ignorar categorías desconocidas. 

Como modelo base (baseline), se evaluó un `DummyClassifier` utilizando la estrategia de la clase más frecuente, obteniendo un rendimiento de 0.38 en F1 Macro. Posteriormente, este desempeño fue contrastado con un modelo Support Vector Machine (`SVC` con `C=1` y kernel `scale`), el cual alcanzó un F1 macro de 0.979, demostrando la viabilidad de aprendizaje sobre la partición estratificada. Las validaciones del esquema se consolidaron mediante pruebas unitarias (`pytest`) que aseguran la existencia de columnas críticas y la integridad del target.

---

## 4. Decisión Green AI y Reducción Dimensional (LAB03)

En la segunda fase analítica, el catálogo de modelos se expandió sin alterar la partición de datos inicial, incorporando ensambles como `RandomForestClassifier` y `HistGradientBoostingClassifier`, así como una variante aplicando Análisis de Componentes Principales (PCA). Para explorar la separabilidad topológica de los datos, se generaron dos visualizaciones t-SNE utilizando distintas semillas aleatorias (42 y 7), las cuales confirmaron la existencia de agrupaciones detectables en los datos originales antes de aplicar los clasificadores complejos.

Para la toma de decisiones basada en Green AI, se ejecutaron tres repeticiones temporales para medir con robustez la mediana del tiempo de ajuste (entrenamiento), la latencia de inferencia y el peso del modelo serializado. El modelo que obtuvo el rendimiento predictivo máximo absoluto fue el **`rf_100`** (Random Forest con 100 estimadores), logrando un F1 macro de **0.989**. Sin embargo, al calcular la frontera de Pareto, seleccioné el modelo **`svm_c1`** (Support Vector Machine con C=1) como la alternativa definitiva por su alta eficiencia computacional.

La selección de esta alternativa implica ceder una diferencia absoluta marginal de tan solo **0.01** en la métrica principal de F1 macro (obteniendo un F1 de **0.979**). A cambio de esta mínima concesión predictiva, logramos un ahorro temporal del **80%** en la mediana del tiempo de entrenamiento (pasando de 0.156 segundos a solo 0.031 segundos). Además, en términos de eficiencia de almacenamiento, el modelo seleccionado presenta un tamaño serializado de apenas **41.71 KB**, lo cual representa una reducción dramática frente a los **1833.07 KB** del modelo más pesado (`rf_300`) y los 616.35 KB del modelo de máximo rendimiento. Esta ganancia en eficiencia es crítica para un posible despliegue ágil.

Es importante señalar como limitación que los costos computacionales reportados son contextuales y dependientes de la máquina. El entorno de hardware que respalda estas mediciones constó de un procesador **AMD64 Family 25 Model 68** bajo un sistema **Windows 11**, ejecutando **Python 3.14.6** y **scikit-learn 1.9.1**. Bajo estas condiciones, la alternativa elegida sobre la frontera de Pareto resulta óptima.