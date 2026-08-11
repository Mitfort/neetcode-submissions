-- Write your query below
SELECT p.customer_id, p.customer_name 
FROM 
    (
        SELECT c.customer_id, c.customer_name,
        SUM(CASE WHEN o.product_name = 'A' THEN 1 ELSE 0 END) as purchased_a,
        SUM(CASE WHEN o.product_name = 'B' THEN 1 ELSE 0 END) as purchased_b,
        SUM(CASE WHEN o.product_name = 'C' THEN 1 ELSE 0 END) as purchased_c
        FROM customers c 
        JOIN orders o ON o.customer_id = c.customer_id
        GROUP BY c.customer_id
    ) p 
WHERE p.purchased_a > 0 
AND p.purchased_b > 0
AND p.purchased_c = 0
ORDER BY p.customer_name ASC;
