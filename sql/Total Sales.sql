SELECT
    ROUND(SUM(sales), 2) AS total_sales
FROM sales
WHERE sales IS NOT NULL
  AND sales >= 0;