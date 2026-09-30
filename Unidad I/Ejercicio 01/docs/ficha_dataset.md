# Ficha del dataset · LAB02

- **Dominio:** Epidemiología nutricional y salud preventiva.
- **Unidad de análisis:** Individuo evaluado en hábitos alimenticios, condición física y antropometría.
- **Decisión:** Priorización e intervención en programas de prevención de riesgo metabólico/obesidad.
- **Target:** `NObeyesdad` (Binarizado: 0 = Peso normal / Insuficiente, 1 = Sobrepeso u Obesidad).
- **Error más costoso:** Falso Negativo (clasificar a una persona con sobrepeso/obesidad como saludable, impidiendo la intervención preventiva oportuna).
- **Usuario:** Personal de salud ocupacional, nutricionistas y promotores de salud pública.

---

### Comparación de Candidatos

| Criterio | Candidato A: Obesity Levels (UCI #544) | Candidato B: Heart Disease (Cleveland, UCI) |
|---|---|---|
| **Procedencia** | UCI Machine Learning Repository | UCI Machine Learning Repository |
| **Licencia** | CC BY 4.0 | CC BY 4.0 |
| **Filas / Columnas** | 2,111 filas / 17 columnas | 303 filas / 14 columnas |
| **Target y clases** | `NObeyesdad` (7 clases originales, binarizable a 2) | `target` (0 = Sano, 1 = Enfermo) |
| **Criterio ≥ 500 filas** | Cumple directamente (2,111 filas) | Requiere autorización docente (303 filas) |
| **Tipo de variables** | Mixtas (3 numéricas, 13 categóricas) | Continuas y ordinales codificadas |
| **Riesgo de fuga** | Presencia de `Weight`/`Height` (documentada y controlada) | Nulo; pruebas diagnósticas previas |

**Decisión propuesta:** Se selecciona **Obesity Levels (UCI #544)** por cumplir el umbral de $\ge 500$ filas sin requerir dispensa y permitir demostrar el uso de `ColumnTransformer` (imputación + escalado + OneHotEncoding).