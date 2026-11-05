WITH checks AS (
    SELECT 'row_count' AS check_name, COUNT(*) AS observed, 9800 AS expected
    FROM sales
    UNION ALL
    SELECT 'distinct_row_ids', COUNT(DISTINCT row_id), 9800
    FROM sales
    UNION ALL
    SELECT 'duplicate_complete_rows',
           COALESCE(SUM(duplicate_count - 1), 0),
           0
    FROM (
        SELECT COUNT(*) AS duplicate_count
        FROM sales
        GROUP BY row_id, order_id, order_date, ship_date, ship_mode,
                 customer_id, customer_name, segment, country, city, state,
                 postal_code, region, product_id, category, sub_category,
                 product_name, sales
        HAVING COUNT(*) > 1
    )
    UNION ALL
    SELECT 'missing_required_values',
           COALESCE(SUM(
               order_id IS NULL OR order_date IS NULL OR ship_date IS NULL OR
               ship_mode IS NULL OR customer_id IS NULL OR customer_name IS NULL OR
               segment IS NULL OR country IS NULL OR city IS NULL OR state IS NULL OR
               region IS NULL OR product_id IS NULL OR category IS NULL OR
               sub_category IS NULL OR product_name IS NULL OR sales IS NULL
           ), 0),
           0
    FROM sales
    UNION ALL
    SELECT 'missing_postal_codes', COUNT(*), 11
    FROM sales
    WHERE postal_code IS NULL
    UNION ALL
    SELECT 'invalid_order_dates', COUNT(*), 0
    FROM sales
    WHERE date(order_date) IS NULL
    UNION ALL
    SELECT 'invalid_ship_dates', COUNT(*), 0
    FROM sales
    WHERE date(ship_date) IS NULL
    UNION ALL
    SELECT 'ship_before_order', COUNT(*), 0
    FROM sales
    WHERE date(ship_date) < date(order_date)
    UNION ALL
    SELECT 'negative_sales', COUNT(*), 0
    FROM sales
    WHERE sales < 0
)
SELECT check_name,
       observed,
       expected,
       CASE
           WHEN observed = expected THEN 'PASS'
           WHEN check_name = 'missing_postal_codes'
               THEN 'REVIEW - missing values retained'
           ELSE 'FAIL'
       END AS status
FROM checks
ORDER BY check_name;
