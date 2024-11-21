SELECT DATEPART(quarter, OrderDate) AS Quarter, COUNT(DISTINCT CustomerID) AS Customers
FROM Orders
WHERE OrderDate >= DATEADD(year, -1, GETDATE())
GROUP BY DATEPART(quarter, OrderDate)
ORDER BY Quarter;
