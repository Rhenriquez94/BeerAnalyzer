from scrapper.jumbo import get_jumbo_products
from scrapper.lider import get_lider_products
from scrapper.santa_isabel import get_sta_isabel_products
from scrapper.tottus import get_tottus_products
from pipeline.transform import clean_data
from pipeline.load import save_to_excel
import time

# Configuración de tiempo de espera
start_time = time.time()

if __name__ == "__main__":
 
    print("Iniciando scraping de Jumbo...")
    productos_jumbo = get_jumbo_products()
    
    print("Iniciando scraping de lider...")
    productos_lider = get_lider_products()

    print("Iniciando scraping de Santa Isabel...")
    productos_staisabel = get_sta_isabel_products()

    print("Iniciando scraping de Tottus...")
    productos_tottus = get_tottus_products()

    productos_fin = productos_jumbo + productos_lider + productos_staisabel  + productos_tottus
    
    if productos_fin:
        df = clean_data(productos_fin)
        save_to_excel(df, "productos_totales")
        print(f"Archivo creado! Total de productos obtenidos: {len(df)}")
        end_time = time.time()

        elapsed_seconds = int(end_time - start_time)

        minutes = elapsed_seconds // 60
        seconds = elapsed_seconds % 60

        elapsed_time = end_time - start_time
        print(f"Tiempo de ejecución: {minutes:02d}:{seconds:02d} minutos")
    else:
        print("No se encontraron productos.")




