-- sales table
-- date       amount
-- 2023-01-01 100
-- 2023-01-02 200
-- 2023-01-03 200
-- 2023-01-04 300

SELECT 
    date,
    amount,
    SUM(amount) OVER (
        ORDER BY date 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS sum_amount
FROM sales;

-- Output
-- date	      amount	sum_amount
-- 2023-01-01	100	    300
-- 2023-01-02	200 	500
-- 2023-01-03	200	    700
-- 2023-01-04	300	    500


SELECT 
    date,
    amount,
    SUM(amount) OVER (
        ORDER BY amount 
        RANGE BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS sum_amount
FROM sales;


-- date	        amount	sum_amount
-- 2023-01-01	100 	300
-- 2023-01-02	200 	500
-- 2023-01-03	200 	500
-- 2023-01-04	300 	500