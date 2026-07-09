-- Write your query below
SELECT s.seller_name
FROM seller AS s
LEFT JOIN  orders as o
ON s.seller_id = o.seller_id AND EXTRACT(YEAR FROM o.sale_date) = 2020
WHERE o.sale_date IS NULL
GROUP BY s.seller_name


