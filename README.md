# 🛒 Scraper Jumbo - Cervezas

Este es un pequeño proyecto de scraping que automatiza la recolección de productos del supermercado **Jumbo**, específicamente de la sección de **cervezas** 🍻.

La idea es simple: simular un navegador real, recorrer varias páginas y traerse datos útiles como nombre, marca y precio de cada producto, para finalmente guardarlos en un archivo Excel.

---

## 🚀 ¿Qué hace el script?

- Abre la página de Jumbo usando Selenium
- Navega por las páginas de cervezas (hasta 10 máximo por defecto)
- Extrae:
  - Nombre del producto
  - Marca
  - Precio
  - Fecha de consulta
- Guarda todo en un archivo `.xlsx` con fecha y hora en el nombre

---

## ⚙️ Requisitos

Antes de correr el script, asegurate de tener instalado:

```bash
pip install selenium pandas openpyxl webdriver-manager
```

> 💡 Requiere que tengas Google Chrome instalado.

---

## ▶️ ¿Cómo se ejecuta?

```bash
python scrapper/jumbo.py
```

Después de unos segundos, deberías ver algo como:

```
Archivo Excel guardado como: productos_jumbo_2024-04-02_18-30.xlsx
Total de productos obtenidos: 85
```

---

## 📦 Archivos generados

Se guarda un archivo Excel en la misma carpeta con el nombre:

```
productos_jumbo_YYYY-MM-DD_HH-MM.xlsx
```

Con columnas como:

| producto | marca | precio | categoria | supermercado | fecha_consulta |
|----------|-------|--------|-----------|--------------|----------------|

---

## ✨ Cosas que podrían mejorarse

- Subida automática a AWS S3 ☁️
- Scraping de más categorías 🍷🥫🥩
- Ejecución automática diaria (con Task Scheduler o cron)
- Guardar también en CSV

---

## 🤘 Autor

Creado por **Rodrigo** como parte de un proyecto personal de automatización y scraping 💻

---