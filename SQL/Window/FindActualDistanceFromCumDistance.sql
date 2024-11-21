/*
Problem: Calculate Actual Distance from Cumulative Distance
- Convert cumulative distances to individual trip distances
- Group by car and order by days
- Handle first trip with default 0 distance
*/

-- Input Table Structure:
-- car_travels
-- cars           VARCHAR
-- days           DATE
-- cumulative_distance  DECIMAL

-- Sample Input:
-- cars    days         cumulative_distance
-- Car1    2023-01-01   100
-- Car1    2023-01-02   250
-- Car1    2023-01-03   400

-- Method 1: Using LAG Function
SELECT 
    cars,
    days,
    cumulative_distance,
    cumulative_distance - LAG(cumulative_distance, 1, 0) OVER (
        PARTITION BY cars
        ORDER BY days
    ) AS distance_travelled
FROM car_travels;

-- Method 2: Using Self-Join
SELECT 
    ct1.cars,
    ct1.days,
    ct1.cumulative_distance,
    ct1.cumulative_distance - COALESCE(
        MAX(ct2.cumulative_distance), 
        0
    ) AS distance_travelled
FROM car_travels ct1
LEFT JOIN car_travels ct2 
    ON ct1.cars = ct2.cars
    AND ct2.days < ct1.days
GROUP BY 
    ct1.cars,
    ct1.days,
    ct1.cumulative_distance;

-- Expected Output:
-- cars    days         cumulative_distance    distance_travelled
-- Car1    2023-01-01   100                   100
-- Car1    2023-01-02   250                   150
-- Car1    2023-01-03   400                   150

/* Performance Optimizations:
1. Efficient LAG function for sequential calculation
2. Smart default handling with 0 for first record
3. Consider index on (cars, days)
4. Multiple implementation options
5. Optimal partitioning strategy
*/
