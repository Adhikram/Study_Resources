-- The idea is to generate a report with all the items priced over $90 and the quantity of these items
-- sold by the London-2 branch.
WITH over_90_items AS (
    SELECT DISTINCT item,
        unit_price
    FROM sales
    WHERE unit_price >= 90
),
london2_over_90 AS (
    SELECT o90.item,
        o90.unit_price,
        coalesce(SUM(s.quantity), 0) as total_sold
    FROM over_90_items o90
        LEFT JOIN sales s ON o90.item = s.item
        AND s.branch = 'London-2'
    GROUP BY o90.item,
        o90.unit_price
)
SELECT item,
    unit_price,
    total_sold
FROM london2_over_90;

-- Input
-- sales table
-- branch    date        item  unit_price  quantity
-- London-1  2021-01-01  1     100         3
-- London-2  2021-01-01  1     100         3
-- London-3  2021-01-01  1     100         3
-- London-1  2021-01-01  2     80          2
-- London-2  2021-01-01  2     80          2
-- London-3  2021-01-01  2     80          2
-- London-1  2021-01-01  3     90          1
-- London-2  2021-01-01  3     90          1
-- London-3  2021-01-01  3     90          1

-- Output
-- item  unit_price  total_sold
-- 1     100         3
-- 2     80          2
-- 3     90          1
-- The output shows the items priced over $90 and the quantity of these items sold by the London-2 branch.