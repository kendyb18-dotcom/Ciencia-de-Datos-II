import io
import zipfile
import urllib.request
from pathlib import Path
import pandas as pd

def download_dataset(destination: str = "data/raw/dataset.csv") -> Path:
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    url = "https://archive.ics.uci.edu/static/public/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition.zip"
    
    print("Descargando dataset desde UCI...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req) as resp:
        zip_bytes = io.BytesIO(resp.read())
        with zipfile.ZipFile(zip_bytes) as z:
            csv_nombre = [f for f in z.namelist() if f.endswith('.csv')][0]
            with z.open(csv_nombre) as f:
                df = pd.read_csv(f)
                
    if df.empty:
        raise ValueError("El dataset descargado está vacío.")

    # Binarización del target: 0 = Peso normal / Bajo peso, 1 = Sobrepeso / Obesidad
    clases_control = ['Normal_Weight', 'Insufficient_Weight']
    df['target'] = (~df['NObeyesdad'].isin(clases_control)).astype(int)
    
    df.to_csv(path, index=False)
    print(f"Dataset guardado en: {path.resolve()}")
    return path

if __name__ == "__main__":
    download_dataset()