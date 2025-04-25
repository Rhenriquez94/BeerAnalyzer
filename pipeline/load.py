from datetime import datetime
import os

def save_to_csv(df,supermercado):
    os.makedirs(f"data/{supermercado}", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"data/{supermercado}/{supermercado}_{timestamp}.csv"
    df.to_csv(filename, index=False)
    print(f"Archivo Excel guardado como: {filename}")