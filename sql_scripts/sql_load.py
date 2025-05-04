import pandas as pd
import os
from sqlalchemy import create_engine, text
from connect import connect
import psycopg2

carpeta = "data/productos_totales"

def cargar_csvs_en_raw():
    engine = connect()
    
    archivos_csv = sorted([
        os.path.join(carpeta, f) for f in os.listdir(carpeta) if f.endswith('.csv')
    ], key=os.path.getmtime)

    if not archivos_csv:
        print("⚠️ No se encontraron archivos CSV.")
        return

    archivo_reciente = archivos_csv[-1]
    print(f"📄 Cargando archivo más reciente: {archivo_reciente}")

    df = pd.read_csv(archivo_reciente)
    print(f"🧹 Columnas originales encontradas: {list(df.columns)}")

    # ✅ Limpiar y normalizar nombres de columnas
    df.columns = df.columns.str.strip().str.lower()

    # ✅ Establecer los nombres esperados
    columnas_objetivo = [
        'product_name', 'brand', 'price', 'category', 'market_name',
        'image_url', 'link', 'query_date'
    ]

    # Validación de columnas
    faltantes = [col for col in columnas_objetivo if col not in df.columns]
    if faltantes:
        print(f"❌ No se pueden insertar datos. Faltan columnas: {faltantes}")
        return

    # Reordenar columnas (opcional, pero recomendable)
    df = df[columnas_objetivo]

    try:
        df.to_sql(
            'raw_products',
            engine,
            if_exists='append',
            index=False,
            method='multi'
        )
        print(f"✅ {len(df)} registros insertados en 'raw_products'.")
    except Exception as e:
        print(f"❌ Error insertando en 'raw_products': {e}")
