import pandas as pd


def clean_data(productos):
    df = pd.DataFrame(productos)
    
    # Limpiar columna de precio
    df['precio'] = df['precio'].astype(str)
    df['precio'] = df['precio'].str.replace(r'[$.]', '', regex=True).str.strip()
    df['precio'] = pd.to_numeric(df['precio'], errors='coerce')
    df = df.dropna(subset=['precio'])
    df['precio'] = df['precio'].astype(int)

    # Formatear texto: primera letra en mayúscula, resto en minúscula
    columnas_texto = ['producto', 'marca', 'categoria', 'supermercado']
    for col in columnas_texto:
        df[col] = df[col].astype(str).str.strip().str.capitalize()

    return df