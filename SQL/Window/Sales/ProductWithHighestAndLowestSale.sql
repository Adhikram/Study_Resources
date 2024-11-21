/*
Problem: Identify Products with Extreme Sales Performance
- Find highest and lowest selling product categories
- Calculate total sales for previous year
- Return both extremes in single result set
*/

-- Input Table Structure:
-- SalesData
-- ProductCategory   VARCHAR
-- SalesAmount      DECIMAL
-- SaleDate         DATE

-- Sample Input:
-- ProductCategory    SalesAmount    SaleDate
-- Electronics       1500.00        2023-01-15
-- Clothing          800.00         2023-02-01
-- Books            200.00         2023-03-10

-- Calculate Previous Year Sales
WITH PreviousYearSales AS (
    SELECT 
        ProductCategory,
        SUM(SalesAmount) AS TotalSales
    FROM 
        SalesData
    WHERE 
        SaleDate >= DATEADD(year, -1, GETDATE())
        AND SaleDate < GETDATE()
    GROUP BY 
        ProductCategory
),

-- Rank Sales Performance
RankedSales AS (
    SELECT 
        ProductCategory,
        TotalSales,
        ROW_NUMBER() OVER (ORDER BY TotalSales DESC) AS DescRank,
        ROW_NUMBER() OVER (ORDER BY TotalSales ASC) AS AscRank
    FROM 
        PreviousYearSales
)

-- Get Highest and Lowest Performers
SELECT 
    ProductCategory,
    TotalSales
FROM 
    RankedSales
WHERE 
    DescRank = 1 
    OR AscRank = 1;

-- Expected Output:
-- ProductCategory    TotalSales
-- Electronics       150000.00
-- Books            20000.00

/* Performance Optimizations:
1. Efficient date filtering
2. Single scan for both rankings
3. Consider index on (SaleDate, ProductCategory)
4. Smart use of window functions
5. Optimal CTE structure
*/
