-- Sample sales table structure
-- date       amount
-- 2023-01-01 100
-- 2023-01-02 200
-- 2023-01-03 200
-- 2023-01-04 300

-- Example 1: ROWS BETWEEN
-- ROWS operates on physical rows, regardless of their values
-- Here it sums current row + 1 row before + 1 row after
SELECT 
    date,
    amount,
    SUM(amount) OVER (
        ORDER BY date 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS sum_amount
FROM sales;

-- ROWS output explanation:
-- For 2023-01-01: 100 + 200 = 300 (no preceding row)
-- For 2023-01-02: 100 + 200 + 200 = 500
-- For 2023-01-03: 200 + 200 + 300 = 700
-- For 2023-01-04: 200 + 300 = 500 (no following row)

-- Example 2: RANGE BETWEEN
-- RANGE operates on logical value ranges
-- Here it sums rows with amount values within ±1 of current row
SELECT 
    date,
    amount,
    SUM(amount) OVER (
        ORDER BY amount 
        RANGE BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS sum_amount
FROM sales;

-- RANGE output explanation:
-- For amount=100: 100 + 200 = 300 (200 is within +1 range)
-- For amount=200: 200 + 200 + 300 = 500 (both 200s counted together)
-- For amount=200: 200 + 200 + 300 = 500 (same range as above)
-- For amount=300: 200 + 200 + 300 = 500 (both 200s within -1 range)