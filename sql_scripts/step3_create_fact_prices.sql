-- STEP 3: Crear tabla de hechos fact_prices

-- Borrar si ya existe
DROP TABLE IF EXISTS public.fact_prices;

-- Crear la tabla de hechos
CREATE TABLE public.fact_prices AS
SELECT 
  p.product_id,
  r.price,
  r.query_date::DATE AS price_date,
  CURRENT_TIMESTAMP AS load_timestamp
FROM public.raw_products r
JOIN public.dim_products p 
  ON r.product_market_id = p.product_name || '|' || p.market_name;

-- Crear índices para mejorar consultas
CREATE INDEX idx_fact_product ON public.fact_prices (product_id);
CREATE INDEX idx_fact_date ON public.fact_prices (price_date);
