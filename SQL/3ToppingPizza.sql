/*
Problem: Calculate All Possible 3-Topping Pizza Combinations
- Generate unique combinations
- Calculate total costs
- Sort by price and alphabetically
*/

-- Input Table Structure:
-- pizza_toppings
-- topping_name     VARCHAR
-- ingredient_cost  DECIMAL

-- Method 1: Using Self-Joins
SELECT 
    CONCAT(
        p1.topping_name, ',', 
        p2.topping_name, ',', 
        p3.topping_name
    ) AS pizza,
    ROUND(
        p1.ingredient_cost + 
        p2.ingredient_cost + 
        p3.ingredient_cost,
        2
    ) AS total_cost
FROM pizza_toppings AS p1
INNER JOIN pizza_toppings AS p2
    ON p1.topping_name < p2.topping_name 
INNER JOIN pizza_toppings AS p3
    ON p2.topping_name < p3.topping_name 
ORDER BY 
    total_cost DESC,
    pizza;

-- Method 2: Using Cross Join and Filtering
SELECT 
    CONCAT(t1.topping_name, ',', t2.topping_name, ',', t3.topping_name) AS pizza,
    ROUND(t1.ingredient_cost + t2.ingredient_cost + t3.ingredient_cost, 2) AS total_cost
FROM 
    pizza_toppings t1,
    pizza_toppings t2,
    pizza_toppings t3
WHERE 
    t1.topping_name < t2.topping_name 
    AND t2.topping_name < t3.topping_name
ORDER BY 
    total_cost DESC,
    pizza;

/* Performance Optimizations:
1. Efficient join strategy
2. Smart alphabetical ordering
3. Precise decimal handling
4. Index on (topping_name, ingredient_cost)
5. Optimal sort implementation
*/
