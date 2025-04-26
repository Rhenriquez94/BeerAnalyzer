from datetime import datetime
import os


def save_to_csv(df, carpeta):
    ruta = f"data/{carpeta}"
    os.makedirs(ruta, exist_ok=True)  # CREA la carpeta si no existe
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"{ruta}/{carpeta}_{timestamp}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Archivo CSV guardado como: {filename}")