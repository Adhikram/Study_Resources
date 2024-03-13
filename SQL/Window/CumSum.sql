SELECT Date,
    Sales,
    SUM(Sales) OVER (
        ORDER BY Date
    ) as CumulativeSales
FROM daily_sales;
-- when calculating the cumulative sales for each product category,
--  you may need to reset the cumulative sum whenever the category changes
SELECT Category,
    Date,
    Sales,
    SUM(Sales) OVER (
        PARTITION BY Category
        ORDER BY Date
    ) as CumulativeSales
FROM daily_sales
ORDER BY Category,
    Date;
SELECT Date,
    Sales,
    SUM(Sales) OVER (
        ORDER BY Date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) as RollingCumulativeSales
FROM daily_sales
ORDER BY Date;