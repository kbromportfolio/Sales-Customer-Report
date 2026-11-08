SELECT
    COUNT(DISTINCT order_id) AS distinct_orders
FROM sales
WHERE order_id IS NOT NULL;