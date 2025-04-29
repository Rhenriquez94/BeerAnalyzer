-- STEP 2: Crear tabla de dimensiones dim_products

-- Borrar si ya existe
DROP TABLE IF EXISTS public.dim_products;

-- Crear la tabla
CREATE TABLE public.dim_products AS
SELECT 
  ROW_NUMBER() OVER (ORDER BY product_name, market_name) AS product_id,
  product_name,
  brand,
  category,
  market_name,
  image_url,
  link
FROM (
  SELECT DISTINCT ON (product_name, market_name)
    product_name,
    brand,
    category,
    market_name,
    image_url,
    link
  FROM public.raw_products
  ORDER BY product_name, market_name, query_date DESC
) AS unique_products;

-- Agregar claves primarias y restricciones de unicidad
ALTER TABLE public.dim_products ADD PRIMARY KEY (product_id);
ALTER TABLE public.dim_products ADD CONSTRAINT unq_product_market UNIQUE (product_name, market_name);
