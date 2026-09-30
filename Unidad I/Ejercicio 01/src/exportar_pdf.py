import os
import subprocess
import sys
from pathlib import Path

def exportar():
    # Localización de rutas relativas al proyecto
    ROOT = Path(__file__).resolve().parent.parent
    notebook_path = ROOT / "notebooks" / "ejercicio_01.ipynb"
    reports_dir = ROOT / "reports"
    reports_dir.mkdir(exist_ok=True)
    
    html_salida = reports_dir / "ejercicio_01.html"
    pdf_salida = reports_dir / "Ejercicio_01.pdf"

    # 1. Exportar el notebook ejecutado a HTML
    print("Convirtiendo notebook a HTML...")
    cmd_nbconvert = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "html",
        str(notebook_path),
        "--output-dir", str(reports_dir),
        "--output", "ejercicio_01.html"
    ]
    subprocess.run(cmd_nbconvert, check=True)

    # 2. Localizar ejecutable de Microsoft Edge o Chrome en Windows
    rutas_navegador = [
        Path(os.environ.get("ProgramFiles(x86)", "C:/Program Files (x86)")) / "Microsoft/Edge/Application/msedge.exe",
        Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Microsoft/Edge/Application/msedge.exe",
        Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Google/Chrome/Application/chrome.exe",
        Path(os.environ.get("ProgramFiles(x86)", "C:/Program Files (x86)")) / "Google/Chrome/Application/chrome.exe",
    ]
    
    navegador = next((p for p in rutas_navegador if p.exists()), None)
    
    if not navegador:
        raise FileNotFoundError("No se encontró el ejecutable de Microsoft Edge o Google Chrome.")

    # 3. Impresión a PDF sin interfaz gráfica
    print("Compilando PDF headless con motor web...")
    cmd_pdf = [
        str(navegador),
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_salida}",
        str(html_salida.resolve().as_uri())
    ]
    subprocess.run(cmd_pdf, check=True)
    print(f"Archivo generado con éxito: {pdf_salida}")

if __name__ == "__main__":
    exportar()