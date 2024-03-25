-- Show me life expectancy throughout history in the UK compared to 5 years on either side
select recorded_year,
    age,
    first_value(age) over(
        order by recorded_year range between interval '5' year preceding
            and interval '5' year following
    ) as fv,
    last_value(age) over(
        order by recorded_year range between interval '5' year preceding
            and interval '5' year following
    ) as lv
from life_expectancy;
--Input
-- life_expectancy table
-- recorded_year  age
-- 1543           33
-- 1548           39
-- 1553           40
-- 1558           43
-- 1563           44
-- 1568           45
-- 1573           47
-- 1578           48

-- Output
-- recorded_year  age  fv  lv
-- 1543           33   33  33
-- 1548           39   33  39
-- 1553           40   33  40
-- 1558           43   33  43
-- 1563           44   33  44
-- 1568           45   33  45