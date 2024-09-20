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
RankedSales AS (
    SELECT 
        ProductCategory,
        TotalSales,
        ROW_NUMBER() OVER (ORDER BY TotalSales DESC) AS DescRank,
        ROW_NUMBER() OVER (ORDER BY TotalSales ASC) AS AscRank
    FROM 
        PreviousYearSales
)
SELECT 
    ProductCategory,
    TotalSales
FROM 
    RankedSales
WHERE 
    DescRank = 1 OR AscRank = 1;