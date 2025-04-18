import pandas as pd

def clean_data(productos):
    df = pd.DataFrame(productos)
    df['precio'] = df['precio'].astype(str)
    df['precio'] = df['precio'].str.replace(r'[$.]', '', regex=True).str.strip()
    df['precio'] = pd.to_numeric(df['precio'], errors='coerce')
    df = df.dropna(subset=['precio'])
    df['precio'] = df['precio'].astype(int)

    return df