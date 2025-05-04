


select dp.product_id,dp.product_name,dp.brand,dp.market_name,fp.price,fp.price_date,dp.link 
from dim_products dp
left join fact_prices fp on dp.product_id = fp.product_id
where market_name not in ('Lider') and dp.product_id  = '376'
order by fp.price_date desc;




WITH cambios AS (
  SELECT 
    dp.product_id,
    dp.product_name,
    dp.brand,
    dp.market_name,
    fp.price,
    fp.price_date,
    dp.link,
    LAG(fp.price) OVER (PARTITION BY fp.product_id ORDER BY fp.price_date) AS previous_price
  FROM dim_products dp
  LEFT JOIN fact_prices fp ON dp.product_id = fp.product_id
  WHERE dp.market_name NOT IN ('Lider')
)
SELECT *
FROM cambios
WHERE price IS DISTINCT FROM previous_price
ORDER BY price_date DESC;


