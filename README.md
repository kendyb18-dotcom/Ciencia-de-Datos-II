# Ejercicio 01 · Dataset público y SVM reproducible

**Autor:** Kendy Báez Santos · **Asignatura:** INF-8239 Ciencia de Datos II · **Unidad:** Unidad I  
**Repositorio oficial:** [Ciencia-de-Datos-II](https://github.com/kendyb18-dotcom/Ciencia-de-Datos-II)  
**Ruta del proyecto:** `Ciencia de DatosII/Unidad I/Ejercicio 01`

---

## Descripción general

Implementación de un pipeline modular y reproducible de Machine Learning para la detección de cardiopatías utilizando el dataset clínico *Heart Disease (Cleveland)* de UCI. El flujo integra:

- **Prevención de fuga de datos :** Partición estratificada fija 60/20/20 (entrenamiento, validación y prueba) aplicada antes de cualquier transformación.
- **Preprocesamiento encapsulado:** Imputación por mediana y estandarización de características dentro de un pipeline formal de `scikit-learn`.
- **Cómputo sostenible (*Green AI*):** Reducción de dimensionalidad de 13 a 7 variables mediante Análisis de Componentes Principales (PCA), optimizando el costo computacional de cálculo de hiperplanos sin perder capacidad explicativa.
- **Validación robusta:** Optimización de hiperparámetros de SVM (kernel RBF) mediante `GridSearchCV` estratificado a 5 pliegues exclusivamente sobre el conjunto de entrenamiento.
- **Comparativa contra Baseline:** Evaluación simultánea frente a un `DummyClassifier` mayoritario en las 3 particiones.

---

## Estructura del proyecto

```text
Ejercicio 01/
│
├── .gitignore                      # Exclusión de .venv, __pycache__ y cachés
├── requirements.txt                # Dependencias exactas del proyecto
├── README.md                       # Documentación técnica reproducible
│
├── notebooks/
│   └── ejercicio_01.ipynb          # Cuaderno de presentación y renderizado final
│
├── src/
│   ├── __init__.py                 # Inicializador de paquete Python
│   └── laboratorio_e01.py          # Motor analítico y generación de artefactos
│
├── tests/
│   └── test_pipeline.py            # Suite de pruebas automatizadas con pytest
│
└── reports/                        # Directorio de artefactos generados
    ├── auditoria.json              # Resumen de registros, duplicados y particiones
    ├── diccionario.csv             # Esquema y metadatos de las 14 variables
    ├── seleccion_dataset.md        # Ficha comparativa y justificación de selección
    ├── busqueda_cv.csv             # Historial completo de ajuste de hiperparámetros
    ├── predicciones_prueba.csv     # Detalle de errores e inferencias en test
    ├── matriz_confusion.png        # Gráfico de matriz de confusión en prueba
    ├── conclusion.md               # Conclusión técnica del experimento (414 palabras)
    └── Ejercicio_01.pdf            # Entregable final exportado para la UASD



    ## Instalación y ejecución reproducible

### 1. Clonación del repositorio y navegación
```bash
git clone [https://github.com/kendyb18-dotcom/Ciencia-de-Datos-II.git](https://github.com/kendyb18-dotcom/Ciencia-de-Datos-II.git)
cd "Ciencia-de-Datos-II/Ciencia de DatosII/Unidad I/Ejercicio 01"

2. Creación y activación del entorno virtual
Para Windows:
python -m venv .venv
.venv\Scripts\activate

macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate

3. Instalación de dependencias
pip install -r requirements.txt

4. Verificación de pruebas automatizadas
pytest tests/

