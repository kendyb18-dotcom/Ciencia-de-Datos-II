# Comparación de datasets y solicitud de aprobación

| Criterio | Heart Disease (Cleveland) (propuesto) | Breast Cancer Wisconsin |
|---|---|---|
| Fuente | UCI | UCI |
| Registros / predictores | 303 / 13 | 569 / 30 |
| Problema | Predecir presencia de enfermedad cardíaca | Clasificar tumores como malignos o benignos |
| Licencia | CC BY 4.0 | CC BY 4.0 |
| Faltantes | Sí (representados con '?') | No |
| Ventaja | Permite demostrar técnicas de imputación de nulos dentro del pipeline | Mayor dimensionalidad |

**Pregunta:** ¿Puede un pipeline SVM con reducción dimensional (PCA) detectar enfermedades cardíacas superando un clasificador mayoritario, asegurando la prevención de fuga de datos durante la imputación?

**Decisión propuesta:** Heart Disease (Cleveland). Seleccionado para demostrar el manejo de datos faltantes y la reducción dimensional en un entorno clínico. Aprobación docente: **PENDIENTE**.