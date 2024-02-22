--  Get the monthly revenue for London-1 and London-2

WITH london1_monthly_revenue AS (
  SELECT
    EXTRACT(MONTH FROM date) as month,
    SUM(unit_price * quantity) AS revenue
  FROM sales
  WHERE EXTRACT(YEAR FROM date) = 2021
    AND branch = 'London-1'
  GROUP BY 1
),
london2_monthly_revenue AS (
  SELECT
    EXTRACT(MONTH FROM date) as month,
    SUM(unit_price * quantity) AS revenue
  FROM sales
  WHERE EXTRACT(YEAR FROM date) = 2021
    AND branch = 'London-2'
  GROUP BY 1
)
SELECT
  l1.month,
  l1.revenue + l2.revenue AS london_revenue,
  l1.revenue AS london1_revenue,
  l2.revenue AS london2_revenue
FROM london1_monthly_revenue l1, london2_monthly_revenue l2
WHERE l1.month = l2.month

-- Input
-- sales table
-- branch    date        item  unit_price  quantity
-- London-1  2021-01-01  1     100         3
-- London-2  2021-01-01  1     100         3
-- London-3  2021-01-01  1     100         3
-- London-1  2021-01-01  2     80          2
-- London-2  2021-01-01  2     80          2
-- London-3  2021-01-01  2     80          2

-- Output
-- month  london_revenue  london1_revenue  london2_revenue
-- 1      540             300              240
