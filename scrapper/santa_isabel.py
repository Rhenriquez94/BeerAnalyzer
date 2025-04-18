from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from datetime import datetime
import pandas as pd

def get_sta_isabel_products():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--enable-unsafe-swiftshader")
        options.add_argument("--disable-webgl")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--log-level=3")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.execute_cdp_cmd("Network.setUserAgentOverride", {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        })

        products = []

        # Lista de URLs y sus categorías
        base_urls = [
            ("https://www.santaisabel.cl/vinos-cervezas-y-licores/cervezas?page={}", "Cervezas"),
        ]

        max_pages = 5
        wait = WebDriverWait(driver, 5)  

        # Configuración de reintentos
        MAX_RETRIES = 3
        RETRY_DELAY = 3 

        for base_url, categoria in base_urls:
            page = 1
            while page <= max_pages:
                retries = 0
                success = False

                while retries < MAX_RETRIES and not success:
                    try:
                        driver.get(base_url.format(page))
                        
                        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.product-card-wrap')))
                        
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(10)

                        elements = driver.find_elements(By.CSS_SELECTOR, 'div.product-card-wrap')

                        if not elements:
                            print(f"No se encontraron productos en página {page} de {categoria}")
                            break

                        for el in elements:
                            try:
                                name = el.find_element(By.CSS_SELECTOR, 'a.product-card-name').text.strip() # Nombre
                            except NoSuchElementException:
                                    name = "Nombre no disponible"

                            try:
                                price = el.find_element(By.CSS_SELECTOR, 'span.prices-main-price').text.strip() #Precio
                            except NoSuchElementException:
                                price = "Precio no disponible"

                            try:
                                marca = el.find_element(By.CSS_SELECTOR, 'a.product-card-brand').text.strip() #Marca
                            except NoSuchElementException:
                                marca = "Marca no disponible"
                                

                            products.append({
                                "producto": name,
                                "marca": marca,  
                                "precio": price,
                                "categoria": categoria,
                                "supermercado": "Santa Isabel",
                                "fecha_consulta": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            })

                        success = True
                        page += 1

                    except TimeoutException:
                        retries += 1
                        print(f"Timeout en página {page}. Reintentando ({retries}/{MAX_RETRIES})...")
                        time.sleep(RETRY_DELAY)

                    except Exception as page_error:
                        print(f"Error inesperado en página {page}: {str(page_error)}")
                        retries = MAX_RETRIES  # Forzar salida
                        break

                if not success:
                    print(f"No se pudo procesar la página {page} después de {MAX_RETRIES} intentos.")
                    break

            print(f"Cerveza de SantaIsabel extraída con éxito total:{len(products)} ")
         

        driver.quit()
        return products

    except Exception as e:
        print(f"❌ Error general en get_sta_isabel_products: {str(e)}")
        if 'driver' in locals():
            driver.quit()
        return []
    


# # Ejecutar
# if __name__ == "__main__":
#     productos = get_sta_isabel_products()
#     print(productos)
#     print(f"Total de productos obtenidos: {len(productos)}")


# # ✅ CONVIERTES LA LISTA A UN DATAFRAME
# productos_df = pd.DataFrame(productos)

# # Ahora sí puedes guardarlo como Excel
# filename = "test.xlsx"
# productos_df.to_excel(filename, index=False)

# print(f"✅ Archivo Excel guardado como: {filename}")