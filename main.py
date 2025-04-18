from scrapper.jumbo import get_jumbo_products
from scrapper.lider import get_lider_products
from scrapper.santa_isabel import get_sta_isabel_products
from pipeline.transform import clean_data
from pipeline.load import save_to_excel

if __name__ == "__main__":

    print("Iniciando scraping de Jumbo...")
    productos_jumbo = get_jumbo_products()
    

    print("Iniciando scraping de lider...")
    productos_lider = get_lider_products()

    print("Iniciando scraping de Santa Isabel...")
    productos_staisabel = get_sta_isabel_products()

    productos_fin = productos_jumbo + productos_lider + productos_staisabel
    
    if productos_fin:
        df = clean_data(productos_fin)
        save_to_excel(df, "productos_totales")
        print(f"Archivo creado! Total de productos obtenidos: {len(df)}")
    else:
        print("No se encontraron productos.")
