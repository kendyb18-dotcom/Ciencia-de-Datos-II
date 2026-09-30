import pandas as pd
from pathlib import Path
import json
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def ejecutar():
    # Resolución infalible de ruta
    archivo_actual = Path(__file__).resolve()
    ROOT = archivo_actual.parent.parent
    
    # Apuntamos a la carpeta 'reports'
    reports_dir = ROOT / 'reports'
    reports_dir.mkdir(exist_ok=True)

    # 1. Carga de datos
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
    cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
    df = pd.read_csv(url, header=None, names=cols, na_values='?')
    
    filas_orig = len(df)
    df.drop_duplicates(inplace=True)
    duplicados = filas_orig - len(df)
    
    # Binarización del objetivo
    df['target'] = (df['target'] > 0).astype(int)
    
    X = df.drop('target', axis=1)
    y = df['target']

    # 2. Partición 60/20/20 (Prevención de fuga de datos)
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42, stratify=y)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)

    # 3. Pipelines
    base = DummyClassifier(strategy='most_frequent')
    base.fit(X_train, y_train)

    pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler()),
        ('pca', PCA(n_components=7, random_state=42)),
        ('svm', SVC(probability=True, random_state=42))
    ])

    param_grid = [{'svm__kernel': ['rbf'], 'svm__C': [0.1, 1, 10], 'svm__gamma': ['scale', 0.1, 0.01]}]
    grid = GridSearchCV(pipe, param_grid, cv=5, scoring='f1_macro')
    grid.fit(X_train, y_train)

    # 4. Cálculo de Métricas
    def get_metrics(model, X_set, y_set, part, name):
        pred = model.predict(X_set)
        prob = model.predict_proba(X_set)[:, 1] if hasattr(model, "predict_proba") else [0.5]*len(y_set)
        return {
            'modelo': name, 'particion': part, 'accuracy': accuracy_score(y_set, pred),
            'f1_macro': f1_score(y_set, pred, average='macro'),
            'precision_macro': precision_score(y_set, pred, average='macro', zero_division=0),
            'recall_0': recall_score(y_set, pred, pos_label=0, zero_division=0),
            'recall_1': recall_score(y_set, pred, pos_label=1, zero_division=0),
            'roc_auc': roc_auc_score(y_set, prob)
        }

    res = []
    for n, m in [('Baseline', base), ('SVM', grid.best_estimator_)]:
        for p, x_p, y_p in [('entrenamiento', X_train, y_train), ('validacion', X_val, y_val), ('prueba', X_test, y_test)]:
            res.append(get_metrics(m, x_p, y_p, p, n))

    # 5. Exportar Artefactos a reports/
    with open(reports_dir / 'auditoria.json', 'w') as f:
        json.dump({'filas_originales': filas_orig, 'filas_utilizadas': len(df), 'duplicados_eliminados': duplicados, 'faltantes': int(df.isna().sum().sum()), 'particiones': {'entrenamiento': len(X_train), 'validacion': len(X_val), 'prueba': len(X_test)}}, f, indent=4)
    
    pd.DataFrame({'variable': cols, 'tipo': ['float64']*13 + ['int64'], 'rol': ['predictor']*13 + ['target'], 'descripcion': ['Edad', 'Sexo', 'Tipo de dolor', 'Presión', 'Colesterol', 'Azúcar', 'ECG', 'Frecuencia cardiaca', 'Angina', 'Depresión ST', 'Pendiente', 'Vasos', 'Talasemia', '0=Sano, 1=Enfermo'], 'faltantes': [0]*14}).to_csv(reports_dir / 'diccionario.csv', index=False)
    
    cv_res = pd.DataFrame(grid.cv_results_)
    cv_res['params'] = cv_res['params'].astype(str)
    cv_res.to_csv(reports_dir / 'busqueda_cv.csv', index=False)
    
    errores = X_test.copy()
    errores['real'] = y_test
    errores['prediccion'] = grid.best_estimator_.predict(X_test)
    errores['error'] = errores['real'] != errores['prediccion']
    errores.to_csv(reports_dir / 'predicciones_prueba.csv', index=True)
    
    ConfusionMatrixDisplay.from_predictions(y_test, grid.best_estimator_.predict(X_test), display_labels=['Sano', 'Enfermo'], cmap='Blues')
    plt.savefig(reports_dir / 'matriz_confusion.png')
    plt.close()

    return pd.DataFrame(res)