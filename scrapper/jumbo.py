from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import pandas as pd

def get_jumbo_products():
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

        #Lista de URLs y sus categorías
        base_urls = [
            ("https://www.jumbo.cl/vinos-cervezas-y-licores/cervezas/cervezas-tradicionales?page={}", "Cervezas"),
        ]

        max_pages = 10  # Límite de páginas por categoría
        wait = WebDriverWait(driver, 5)

        # Recorremos cada URL y su categoría
        for base_url, categoria in base_urls:
            page = 1
            while page <= max_pages:
                try:
                    driver.get(base_url.format(page))
                    
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-card-wrap")))
                    
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)

                    elements = driver.find_elements(By.CLASS_NAME, "product-card-wrap")
                    if not elements:
                        break

                    for el in elements:
                        try:
                            name = el.find_element(By.CLASS_NAME, "product-card-name").text.strip()
                        except:
                            name = "No disponible"

                        try:
                            brand = el.find_element(By.CLASS_NAME, "product-card-brand").text.strip()
                        except:
                            brand = "No disponible"

                        try:
                            price = el.find_element(By.CLASS_NAME, "area-price-regular span").text.strip()
                        except:
                            price = "No disponible"

                        try:
                            image_url = el.find_element(By.TAG_NAME, "source").get_attribute("srcset")
                        except:
                            image_url = ""

                        try:
                            url = el.find_element(By.TAG_NAME, "a").get_attribute("href")
                        except:
                            url = ""

                        products.append({
                            "producto": name,
                            "marca": brand,
                            "precio": price,
                            "categoria": categoria,   
                            "supermercado": "Jumbo",
                            "image_url": image_url,
                            "url": url,
                            "fecha_consulta": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })

                    page += 1

                except Exception as page_error:
                    print(f"Error en página {page} de categoría {categoria}: {str(page_error)}")
                    break
            print(f"Cerveza de Jumbo extraída con éxito total:{len(products)} ")


        driver.quit()
        return products

    except Exception as e:
        print(f"Error general en get_jumbo_products: {str(e)}")
        if 'driver' in locals():
            driver.quit()
        return []

