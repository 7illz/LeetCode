# Write your MySQL query statement below

-- Scenario 1: Products that had a price change on or before 2019-08-16
SELECT 
    product_id, 
    new_price AS price
FROM 
    Products
WHERE 
    (product_id, change_date) IN (
        SELECT 
            product_id, 
            MAX(change_date) 
        FROM 
            Products 
        WHERE 
            change_date <= '2019-08-16' 
        GROUP BY 
            product_id
    )

UNION

-- Scenario 2: Products that had NO price changes on or before 2019-08-16
SELECT DISTINCT 
    product_id, 
    10 AS price
FROM 
    Products
WHERE 
    product_id NOT IN (
        SELECT 
            product_id 
        FROM 
            Products 
        WHERE 
            change_date <= '2019-08-16'
    );