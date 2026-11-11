import os
from importlib import import_module

# Importa la funcion del script de simulacion (no se copia el codigo de generacion).
simular = import_module("simular_prioridades")

# Carpeta y rutas de salida.
CARPETA = "data/crudo"
RUTA_CSV = os.path.join(CARPETA, "prioridades_sucio.csv")
RUTA_XLSX = os.path.join(CARPETA, "prioridades_sucio.xlsx")
RUTA_JSON = os.path.join(CARPETA, "prioridades_sucio.json")


def exportar():
    # La carpeta se crea sola si no existe.
    os.makedirs(CARPETA, exist_ok=True)

    df = simular.generar_prioridades(200)

    df.to_csv(RUTA_CSV, index=False, encoding="utf-8")
    df.to_excel(RUTA_XLSX, index=False, sheet_name="prioridades")
    df.to_json(RUTA_JSON, orient="records", force_ascii=False, indent=2)

    # Ruta y tamano (shape) de cada archivo generado.
    for ruta in (RUTA_CSV, RUTA_XLSX, RUTA_JSON):
        print(f"{ruta} -> {df.shape}")


if __name__ == "__main__":
    exportar()