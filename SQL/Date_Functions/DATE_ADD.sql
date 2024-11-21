/*
Problem: Demonstrate DATE_ADD/DATEADD Function Usage
- Add intervals to dates
- Handle different time units
- Support various business scenarios
*/

-- Input Table Structure:
-- events
-- event_id    INT
-- event_date  DATE
-- event_type  VARCHAR

-- Basic Interval Addition
SELECT 
    event_date,
    DATEADD(day, 1, event_date) AS next_day,
    DATEADD(week, 1, event_date) AS next_week,
    DATEADD(month, 1, event_date) AS next_month,
    DATEADD(year, 1, event_date) AS next_year
FROM events;

-- Business Use Cases
SELECT
    order_date,
    -- Delivery estimation
    DATEADD(day, 3, order_date) AS estimated_delivery,
    -- Subscription renewal
    DATEADD(month, 1, subscription_start) AS next_billing_date,
    -- Warranty expiration
    DATEADD(year, 2, purchase_date) AS warranty_end
FROM orders;

-- Rolling Date Windows
SELECT 
    current_date AS today,
    DATEADD(day, -7, current_date) AS last_week,
    DATEADD(month, -1, current_date) AS last_month,
    DATEADD(year, -1, current_date) AS last_year
FROM dual;

-- Expected Output:
-- today        last_week     last_month    last_year
-- 2024-01-20   2024-01-13   2023-12-20    2023-01-20

/* Performance Optimizations:
1. Use for date range queries
2. Index friendly for range scans
3. Combine with appropriate date indexes
4. Consider time zone implications
5. Use for partition pruning
*/
