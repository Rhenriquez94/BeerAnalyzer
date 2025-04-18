from datetime import datetime
import os

def save_to_excel(df,supermercado):
    os.makedirs(f"data/{supermercado}", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"data/{supermercado}/{supermercado}_{timestamp}.xlsx"
    df.to_excel(filename, index=False)
    print(f"Archivo Excel guardado como: {filename}")