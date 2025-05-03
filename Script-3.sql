WITH productos_con_cambio AS (
    SELECT 
        fp.product_id
    FROM fact_prices fp
    GROUP BY fp.product_id
    HAVING COUNT(DISTINCT fp.price) > 1
)

SELECT 
    dp.product_id,
    dp.product_name,
    dp.brand,
    dp.market_name,
    fp.price,
    fp.price_date
FROM productos_con_cambio pc
INNER JOIN dim_products dp ON dp.product_id = pc.product_id
INNER JOIN fact_prices fp ON dp.product_id = fp.product_id
ORDER BY dp.product_id, fp.price_date;


select distinct dp.product_id,dp.product_name ,dp.market_name ,fp.price ,fp.price_date,dp.link 
from 
dim_products dp left join fact_prices fp 
on dp.product_id = fp.product_id
where dp.product_id  = 499
order by fp.price_date asc



select * from raw_products rp 
where product_name = 'Cerveza trooper amber ale 4.7° 500 cc';






