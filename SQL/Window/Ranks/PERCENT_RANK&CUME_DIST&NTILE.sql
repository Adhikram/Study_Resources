-- Show me distributions of Hollywood movie box office sales using PERCENT_RANK, CUME_DIST, and NTILE (quartile, decile, tertile, etc)
select name,
    gross_sales,
    percent_rank() over(
        order by gross_sales
    ) as pct,
    cume_dist() over(
        order by gross_sales
    ) as cum_dist,
    ntile(4) over(
        order by gross_sales
    ) as ntil
from movies;

-- Input
-- movies table
-- name          gross_sales
-- Movie 1       100
-- Movie 2       200
-- Movie 3       300
-- Movie 4       400
-- Movie 5       500

-- Output
-- name      gross_sales  pct  cum_dist  ntil
-- Movie 1   100          0.0  0.2       1
-- Movie 2   200          0.25 0.4       1
-- Movie 3   300          0.5  0.6       2
-- Movie 4   400          0.75 0.8       3
-- Movie 5   500          1.0  1.0       4