from pathlib import Path
import pandas as pd

TARGET = "target"
REQUIRED = {TARGET, "Age", "Height", "Weight", "Gender", "MTRANS"}

def load_data():
    # Buscar data/raw/dataset.csv en la ruta relativa actual o superior
    cwd = Path.cwd().resolve()
    ruta_candidata = cwd / "data" / "raw" / "dataset.csv"
    if not ruta_candidata.exists():
        ruta_candidata = cwd.parent / "data" / "raw" / "dataset.csv"
    
    assert ruta_candidata.exists(), f"El archivo no existe en: {ruta_candidata}"
    return pd.read_csv(ruta_candidata)

def test_dataset_is_not_empty():
    df = load_data()
    assert not df.empty, "El dataset está vacío"
    assert len(df) >= 500, f"Debe tener al menos 500 filas. Filas actuales: {len(df)}"

def test_required_columns_exist():
    df = load_data()
    assert REQUIRED <= set(df.columns), f"Faltan columnas clave: {REQUIRED - set(df.columns)}"

def test_target_has_no_missing_and_two_classes():
    y = load_data()[TARGET]
    assert y.notna().all(), "El target contiene valores nulos"
    assert y.nunique() >= 2, "El target debe tener al menos dos clases"