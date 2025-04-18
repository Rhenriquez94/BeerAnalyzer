import pandas as pd

def clean_data(productos):
    df = pd.DataFrame(productos)
    df['precio'] = df['precio'].str.replace('[$.]', '', regex=True).str.strip()
    df['precio'] = pd.to_numeric(df['precio'], errors='coerce')
    return df