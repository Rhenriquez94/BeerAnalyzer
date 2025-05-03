from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import pandas as pd

def get_jumbo_products():
    try:
        # Configuración de Chrome para headless en servidores
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-infobars")
        options.add_argument("--window-size=1920,1080")

        # Usa el ChromeDriver instalado manualmente
        service = Service("/usr/local/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)

        products = []

        base_urls = [
            ("https://www.jumbo.cl/vinos-cervezas-y-licores/cervezas/cervezas-tradicionales?page={}", "Cervezas"),
        ]

        max_pages = 10
        wait = WebDriverWait(driver, 8)

        for base_url, categoria in base_urls:
            page = 1
            while page <= max_pages:
                try:
                    driver.get(base_url.format(page))
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-card")))

                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(8)

                    elements = driver.find_elements(By.CLASS_NAME, "product-card")
                    if not elements:
                        break

                    for el in elements:
                        driver.execute_script("arguments[0].scrollIntoView();", el)
                        time.sleep(0.2)

                        name = el.find_element(By.CLASS_NAME, "product-card-name").text.strip() if el.find_elements(By.CLASS_NAME, "product-card-name") else "No disponible"
                        brand = el.find_element(By.CLASS_NAME, "product-card-brand").text.strip() if el.find_elements(By.CLASS_NAME, "product-card-brand") else "No disponible"
                        try:
                            price = el.find_element(By.CSS_SELECTOR, ".area-price-regular span").text.strip()
                        except:
                            price = "No disponible"
                        image_url = el.find_element(By.TAG_NAME, "source").get_attribute("srcset") if el.find_elements(By.TAG_NAME, "source") else ""
                        link = el.find_element(By.XPATH, ".//ancestor::a").get_attribute("href") if el.find_elements(By.XPATH, ".//ancestor::a") else ""

                        products.append({
                            "product_name": name,
                            "brand": brand,
                            "price": price,
                            "category": categoria,
                            "market_name": "Jumbo",
                            "image_url": image_url,
                            "link": link,
                            "query_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })

                    page += 1

                except Exception as page_error:
                    print(f"⚠️ Error en página {page} de {categoria}: {str(page_error)}")
                    break

        driver.quit()
        print(f"✅ Cerveza de Jumbo extraída con éxito: {len(products)} productos.")
        return products

    except Exception as e:
        print(f"❌ Error general en get_jumbo_products: {str(e)}")
        if 'driver' in locals():
            driver.quit()
        return []

# Ejecución directa para prueba
if __name__ == "__main__":
    productos = get_jumbo_products()
    df = pd.DataFrame(productos)
    df.to_excel("jumbo_productos.xlsx", index=False)
    print("✅ Archivo guardado: jumbo_productos.xlsx")
