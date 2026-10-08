from pathlib import Path
import io
import json
import ssl
import urllib.request

import pandas as pd


UCI_API_BASE_URL = "https://archive.ics.uci.edu/api/dataset"


def _fetch_bytes(url: str) -> bytes:
    """Descarga contenido sin validar el certificado SSL."""
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(request, context=context, timeout=60) as response:
        return response.read()


def download_uci_dataset(uci_id: int, destination="data/raw/dataset.csv") -> Path:
    """Descarga un dataset desde UCI Machine Learning Repository."""
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)

    metadata = json.loads(_fetch_bytes(f"{UCI_API_BASE_URL}?id={uci_id}").decode("utf-8"))
    if metadata.get("status") != 200:
        raise ValueError(metadata.get("message", f"No se encontró el dataset con id={uci_id}"))

    data_url = metadata["data"]["data_url"]
    if not data_url:
        raise ValueError(f"El dataset {uci_id} no tiene un CSV disponible para descarga")

    frame = pd.read_csv(io.BytesIO(_fetch_bytes(data_url)))
    if frame.empty:
        raise ValueError("El dataset descargado está vacío")

    frame.to_csv(path, index=False)
    return path

# Ejecutar la descarga encapsulada
path = download_uci_dataset(uci_id=529)
print(f"Dataset descargado y guardado exitosamente en: {path}")
