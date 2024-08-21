-- Solution:
with recursive cte as (
    select id,
        item_name,
        total_count,
        1 as level
    from travel_items
    union all
    select cte.id,
        cte.item_name,
        cte.total_count - 1,
        level + 1 as level
    from cte
        join travel_items t on t.item_name = cte.item_name
        and t.id = cte.id
    where cte.total_count > 1
)
select id,
    item_name
from cte
order by 1;
-- Input:
-- travel_items table
-- +----+-----------+-------------+
-- | id | item_name | total_count |
-- +----+-----------+-------------+
-- | 1  | Bag       | 2           |
-- | 2  | Shoes     | 1           |
-- | 3  | Bag       | 1           |
-- | 4  | Shoes     | 2           |
-- +----+-----------+-------------+
-- Output:
-- +----+-----------+
-- | id | item_name |
-- +----+-----------+
-- | 1  | Bag       |
-- | 1  | Bag       |
-- | 2  | Shoes     |
-- | 4  | Shoes     |
-- +----+-----------+