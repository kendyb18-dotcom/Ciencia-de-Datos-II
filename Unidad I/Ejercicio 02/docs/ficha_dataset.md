# Ficha del dataset

- **Dominio:** Salud clínica y epidemiología.
- **Unidad de análisis:** Un paciente individual.
- **Decisión:** Asignación de intervenciones médicas preventivas tempranas o priorización de atención clínica.
- **Target:** Diagnóstico de riesgo o presencia de diabetes (Positivo / Negativo).
- **Error más costoso:** Falso negativo (clasificar a un paciente en riesgo como sano, retrasando u omitiendo un tratamiento temprano crucial).
- **Usuario:** Personal médico, endocrinólogos o analistas de salud pública.

## Enlaces Obligatorios
- **URL de la ficha (Documentación):** https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset
- **URL de descarga directa:** Se requiere usar la API de la librería `ucimlrepo` en lugar de una URL de descarga en texto plano para este repositorio.

## Comparación de Candidatos

| Criterio | Candidato A: Early Stage Diabetes Risk | Candidato B: Hypertension Risk Prediction |
| :--- | :--- | :--- |
| **Procedencia** | UCI Machine Learning Repository | Repositorio Kaggle / OpenML |
| **Licencia** | Uso académico libre (CC BY 4.0) | Dominio Público (CC0 / Open Data) |
| **Filas/columnas** | 520 filas / 17 columnas | ~1,985 filas / 11 columnas |
| **Target y clases** | class (2 clases: Positivo, Negativo) | hypertension o Risk_Level (2 clases: Presente, Ausente) |
| **Ausentes** | Ninguno (previamente curado) | Mínimos (requerirá imputación básica) |
| **Riesgo de fuga** | Bajo (síntomas iniciales previos al diagnóstico) | Bajo (parámetros clínicos rutinarios) |

