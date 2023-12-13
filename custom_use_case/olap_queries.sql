-- Total Sales by Category for a Given Year
SELECT 
    "Category", 
    SUM("TotalPrice") AS "TotalSales"
FROM "sales"
JOIN "products" ON "sales"."ProductID" = "products"."ProductID"
WHERE date_part('year', "SaleDate"::timestamp) = 2023
GROUP BY "Category";


-- Monthly Sales Trend for a Specific Product
SELECT 
    MONTH(SaleDate) as Month, 
    SUM(TotalPrice) as MonthlySales
FROM Sales
WHERE ProductID = [SpecificProductID]
GROUP BY MONTH(SaleDate);


-- Top 10 Customers by Sales Volume
SELECT 
    "Customers"."CustomerName", 
    SUM("Sales"."TotalPrice") AS "TotalSpent"
FROM "Sales"
JOIN "Customers" ON "Sales"."CustomerID" = "Customers"."CustomerID"
GROUP BY "Sales"."CustomerID"
ORDER BY "TotalSpent" DESC
LIMIT 10;


-- Stock Analysis - Products Close to Stock Out
SELECT 
    "ProductName", 
    "StockQuantity"
FROM "Products"
WHERE "StockQuantity" < [ThresholdValue]  -- Replace [ThresholdValue] with the actual threshold value
ORDER BY "StockQuantity" ASC;


-- Sales Performance by Region
SELECT "Customers"."Location", SUM("Sales"."TotalPrice") AS "RegionSales"
FROM "Sales"
JOIN "Customers" ON "Sales"."CustomerID" = "Customers"."CustomerID"
GROUP BY "Customers"."Location";