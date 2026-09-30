import pytest
import sys
from pathlib import Path

# Resolución robusta de la ruta
cwd = Path.cwd().resolve()
if cwd.name == 'tests':
    ROOT = cwd.parent
elif cwd.name == 'Ciencia de DatosII':
    ROOT = cwd / 'Unidad I' / 'Ejercicio 01'
else:
    ROOT = cwd

sys.path.insert(0, str(ROOT / 'src'))
from laboratorio_e01 import ejecutar

# Fixture para ejecutar el motor una sola vez y reutilizar el resultado
@pytest.fixture(scope="module")
def resultados():
    return ejecutar()

# PRUEBA 1
def test_ejecucion_no_vacia(resultados):
    """Prueba 1: Verifica que el motor retorne datos validos."""
    assert not resultados.empty, "El dataframe de resultados no debe estar vacío"

# PRUEBA 2
def test_metricas_completas(resultados):
    """Prueba 2: Verifica que existan las métricas clave."""
    columnas_requeridas = ['modelo', 'particion', 'f1_macro', 'roc_auc']
    for col in columnas_requeridas:
        assert col in resultados.columns, f"Falta la métrica clave: {col}"

# PRUEBA 3
def test_volumen_particiones(resultados):
    """Prueba 3: Verifica que existan resultados para Baseline y SVM en las 3 particiones."""
    assert len(resultados) == 6, "Deben existir exactamente 6 filas de resultados"