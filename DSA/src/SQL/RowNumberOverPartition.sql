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
-- Difference between ROW_NUMBER() and RANK()
-- The ROW_NUMBER() and RANK() functions are similar in that they both assign a rank to each row based on the order of the ordering column within each partition.
-- However, the main difference between the two functions is how they handle ties.
-- The ROW_NUMBER() function assigns a unique rank to each row, even if there are ties, while the RANK() function leaves gaps in the ranking sequence when there are ties.
-- For example, if there are two rows with the same salary, the ROW_NUMBER() function would assign them ranks 1 and 2,
-- while the RANK() function would assign them both rank 1.
