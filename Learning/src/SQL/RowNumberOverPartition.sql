-- we obtain a report to inform each branch of the date on which the largest ticket (i.e., amount of the item - quantity combination) was sold
-- and the amount of this ticket 
WITH tickets AS (
    SELECT distinct branch,
        date,
        unit_price * quantity AS ticket_amount,
        ROW_NUMBER() OVER (
            PARTITION BY branch
            ORDER by unit_price * quantity DESC
        ) AS position
    FROM sales
    ORDER BY 3 DESC
)
SELECT branch,
    date,
    ticket_amount
FROM tickets
WHERE position = 1

-- Input
-- sales table
-- branch  date        item  unit_price  quantity
-- London-1  2021-01-01  1     100         3
-- London-2  2021-01-01  1     100         3
-- London-3  2021-01-01  1     100         3

-- Output
-- branch    date        ticket_amount
-- London-1  2021-01-01  300
-- London-2  2021-01-01  300
-- London-3  2021-01-01  300

