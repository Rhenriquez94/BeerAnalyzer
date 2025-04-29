import pandas as pd
import os
from sqlalchemy import create_engine, text
from connect import connect
import psycopg2

# Carpeta donde están tus CSVs
carpeta = "data/productos_totales"

def cargar_csvs_en_raw():
    # Conectarse solo una vez
    engine = connect()
    
    # Obtener lista de archivos CSV ordenados por fecha de modificación
    archivos_csv = sorted([
        os.path.join(carpeta, f) for f in os.listdir(carpeta) if f.endswith('.csv')
    ], key=os.path.getmtime)

    if not archivos_csv:
        print("No se encontraron archivos CSV.")
        return

    # Seleccionar el más reciente
    archivo_reciente = archivos_csv[-1]
    print(f"📄 Cargando archivo más reciente: {archivo_reciente}")

    # Leer el CSV
    df = pd.read_csv(archivo_reciente)
    print(f"🧹 Columnas encontradas: {list(df.columns)}")

    # Insertar en la tabla raw_products
    try:
        df.to_sql(
            'raw_products',
            engine,  # Usamos el engine ya conectado
            if_exists='append',
            index=False,
            method='multi'
        )
        print(f"✅ {len(df)} registros insertados en 'raw_products'.")
    except Exception as e:
        print(f"❌ Error insertando en 'raw_products': {e}")


