-- STEP 1: Agregar columna de ID único en raw_products

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_name = 'raw_products' AND column_name = 'product_market_id'
    ) THEN
        ALTER TABLE public.raw_products ADD COLUMN product_market_id VARCHAR(255);
    END IF;
END
$$;

-- Rellenar la nueva columna product_market_id
UPDATE public.raw_products
SET product_market_id = product_name || '|' || market_name
WHERE product_market_id IS NULL;
