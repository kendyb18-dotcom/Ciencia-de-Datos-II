from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

import pandas as pd

# Enlace directo al CSV del dataset UCI 529
url = "https://archive.ics.uci.edu/static/public/529/data.csv"
request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

with urlopen(request, timeout=60) as response:
    df = pd.read_csv(BytesIO(response.read()))

# Guarda el archivo en data/raw, tanto si el notebook está en notebooks/
# como si se ejecuta desde la carpeta raíz del proyecto.
current_dir = Path.cwd()
project_root = current_dir.parent if current_dir.name == "notebooks" else current_dir
destination = project_root / "data" / "raw" / "dataset.csv"

destination.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(destination, index=False)

print(f"Dataset descargado y guardado en: {destination}")
print(f"Filas y columnas: {df.shape}")


