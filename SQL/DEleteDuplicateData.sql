-- Solution 1:
delete from cars
where model_id not in (
        select min(model_id)
        from cars
        group by model_name,
            brand
    );
-- Solution 2:
delete from cars
where ctid in (
        select max(ctid)
        from cars
        group by model_name,
            brand
        having count(1) > 1
    );
-- Solution 3:
with duplicates as (
    select model_id
    from (
        select model_id,
            row_number() over(
                partition by model_name, brand
                order by model_id
            ) as rn
        from cars
    ) x
    where x.rn > 1
)
delete from cars
where model_id in (select model_id from duplicates);