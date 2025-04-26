import pandas as pd
import os
from sqlalchemy import create_engine
import psycopg2



engine = create_engine("postgresql+psycopg2://postgres:123@localhost:5432/beer_analyzer")

# try:
#     # Consulta de prueba
#     df = pd.read_sql("SELECT NOW() as conexion_exitosa", engine)
#     print(df)
#     print("✅ Conexión exitosa a la base de datos.")
# except Exception as e:
#     print("Error al conectar con la base de datos:")
#     print(e)


carpeta = "data/productos_totales"

def cargar_csvs_en_raw():
  # Obtener lista de archivos CSV ordenados por fecha de modificación
    archivos_csv = sorted([
        os.path.join(carpeta, f) for f in os.listdir(carpeta) if f.endswith('.csv')
    ], key=os.path.getmtime)

    if not archivos_csv:
        print("No se encontraron archivos CSV.")
        return

    # Seleccionar el más reciente
    archivo_reciente = archivos_csv[-1]
    print(f" Cargando archivo más reciente: {archivo_reciente}")

    # Leer el CSV
    df = pd.read_csv(archivo_reciente)
    print(df.columns)


    # Insertar en la tabla raw_products
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




