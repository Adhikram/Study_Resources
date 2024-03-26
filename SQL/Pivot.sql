select customer_id
, case when Jan_21 < 0 then '(' || (Jan_21 * -1) || ')$' else Jan_21 || '$' end as "Jan-21"
, case when Feb_21 < 0 then '(' || (Feb_21 * -1) || ')$' else Feb_21 || '$' end as "Feb-21"
, case when Mar_21 < 0 then '(' || (Mar_21 * -1) || ')$' else Mar_21 || '$' end as "Mar-21"
, case when Apr_21 < 0 then '(' || (Apr_21 * -1) || ')$' else Apr_21 || '$' end as "Apr-21"
, case when May_21 < 0 then '(' || (May_21 * -1) || ')$' else May_21 || '$' end as "May-21"
, case when Jun_21 < 0 then '(' || (Jun_21 * -1) || ')$' else Jun_21 || '$' end as "Jun-21"
, case when Jul_21 < 0 then '(' || (Jul_21 * -1) || ')$' else Jul_21 || '$' end as "Jul-21"
, case when Aug_21 < 0 then '(' || (Aug_21 * -1) || ')$' else Aug_21 || '$' end as "Aug-21"
, case when Sep_21 < 0 then '(' || (Sep_21 * -1) || ')$' else Sep_21 || '$' end as "Sep-21"
, case when Oct_21 < 0 then '(' || (Oct_21 * -1) || ')$' else Oct_21 || '$' end as "Oct-21"
, case when Nov_21 < 0 then '(' || (Nov_21 * -1) || ')$' else Nov_21 || '$' end as "Nov-21"
, case when Dec_21 < 0 then '(' || (Dec_21 * -1) || ')$' else Dec_21 || '$' end as "Dec-21"
, case when total < 0 then '(' || (total * 1) || ')$' else total || '$' end as total
from (
    select customer_id
    , sum(case when date_format(sales_date,'%b-%y') = 'Jan-21' then replace(amount,'$','') else 0 end) as Jan_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Feb-21' then replace(amount,'$','') else 0 end) as Feb_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Mar-21' then replace(amount,'$','') else 0 end) as Mar_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Apr-21' then replace(amount,'$','') else 0 end) as Apr_21
    , sum(case when date_format(sales_date,'%b-%y') = 'May-21' then replace(amount,'$','') else 0 end) as May_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Jun-21' then replace(amount,'$','') else 0 end) as Jun_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Jul-21' then replace(amount,'$','') else 0 end) as Jul_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Aug-21' then replace(amount,'$','') else 0 end) as Aug_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Sep-21' then replace(amount,'$','') else 0 end) as Sep_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Oct-21' then replace(amount,'$','') else 0 end) as Oct_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Nov-21' then replace(amount,'$','') else 0 end) as Nov_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Dec-21' then replace(amount,'$','') else 0 end) as Dec_21
    , sum(replace(amount,'$','')) as total
    from sales_data
    group by customer_id
        union
    select 'Total' as customer_id
    , sum(case when date_format(sales_date,'%b-%y') = 'Jan-21' then replace(amount,'$','') else 0 end) as Jan_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Feb-21' then replace(amount,'$','') else 0 end) as Feb_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Mar-21' then replace(amount,'$','') else 0 end) as Mar_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Apr-21' then replace(amount,'$','') else 0 end) as Apr_21
    , sum(case when date_format(sales_date,'%b-%y') = 'May-21' then replace(amount,'$','') else 0 end) as May_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Jun-21' then replace(amount,'$','') else 0 end) as Jun_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Jul-21' then replace(amount,'$','') else 0 end) as Jul_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Aug-21' then replace(amount,'$','') else 0 end) as Aug_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Sep-21' then replace(amount,'$','') else 0 end) as Sep_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Oct-21' then replace(amount,'$','') else 0 end) as Oct_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Nov-21' then replace(amount,'$','') else 0 end) as Nov_21
    , sum(case when date_format(sales_date,'%b-%y') = 'Dec-21' then replace(amount,'$','') else 0 end) as Dec_21
    , null as total
    from sales_data
    ) x
order by 1;

-- Solution in MSSQL using Pivot
select customer_id
, case when Jan_21<0 then concat( '(' , (Jan_21*-1) , ')$' ) else concat( Jan_21 , '$' ) end as Jan_21
, case when Feb_21<0 then concat( '(' , (Feb_21*-1) , ')$' ) else concat( Feb_21 , '$' ) end as Feb_21
, case when Mar_21<0 then concat( '(' , (Mar_21*-1) , ')$' ) else concat( Mar_21 , '$' ) end as Mar_21
, case when Apr_21<0 then concat( '(' , (Apr_21*-1) , ')$' ) else concat( Apr_21 , '$' ) end as Apr_21
, case when May_21<0 then concat( '(' , (May_21*-1) , ')$' ) else concat( May_21 , '$' ) end as May_21
, case when Jun_21<0 then concat( '(' , (Jun_21*-1) , ')$' ) else concat( Jun_21 , '$' ) end as Jun_21
, case when Jul_21<0 then concat( '(' , (Jul_21*-1) , ')$' ) else concat( Jul_21 , '$' ) end as Jul_21
, case when Aug_21<0 then concat( '(' , (Aug_21*-1) , ')$' ) else concat( Aug_21 , '$' ) end as Aug_21
, case when Sep_21<0 then concat( '(' , (Sep_21*-1) , ')$' ) else concat( Sep_21 , '$' ) end as Sep_21
, case when Oct_21<0 then concat( '(' , (Oct_21*-1) , ')$' ) else concat( Oct_21 , '$' ) end as Oct_21
, case when Nov_21<0 then concat( '(' , (Nov_21*-1) , ')$' ) else concat( Nov_21 , '$' ) end as Nov_21
, case when Dec_21<0 then concat( '(' , (Dec_21*-1) , ')$' ) else concat( Dec_21 , '$' ) end as Dec_21
, case when customer_id = 'Total' then null
       else case when total < 0 then concat( '(' , (total*-1) , ')$' ) else concat( total , '$' ) end
  end as total
from (
    select a.*
    , (Jan_21 + Feb_21 + Mar_21 + Apr_21 + May_21 + Jun_21
    + Jul_21 + Aug_21 + Sep_21 + Oct_21 + Nov_21 + Dec_21) as total
    from (
        select customer_id
            , coalesce([Jan-21],0) as Jan_21
            , coalesce([Feb-21],0) as Feb_21
            , coalesce([Mar-21],0) as Mar_21
            , coalesce([Apr-21],0) as Apr_21
            , coalesce([May-21],0) as May_21
            , coalesce([Jun-21],0) as Jun_21
            , coalesce([Jul-21],0) as Jul_21
            , coalesce([Aug-21],0) as Aug_21
            , coalesce([Sep-21],0) as Sep_21
            , coalesce([Oct-21],0) as Oct_21
            , coalesce([Nov-21],0) as Nov_21
            , coalesce([Dec-21],0) as Dec_21
            from (
                select customer_id, format(sales_date, 'MMM-yy') as month, cast(replace(amount,'$','') as int) as amount
                from sales_data s
                ) as x
            pivot
            (
            sum(amount)
            for month in ([Jan-21], [Feb-21], [Mar-21], [Apr-21]
                            ,[May-21], [Jun-21] , [Jul-21], [Aug-21]
                            ,[Sep-21], [Oct-21] , [Nov-21], [Dec-21] )
            ) as y
            ) a
    union
    select 'Total' as customer_id
            , coalesce([Jan-21],0) as Jan_21
            , coalesce([Feb-21],0) as Feb_21
            , coalesce([Mar-21],0) as Mar_21
            , coalesce([Apr-21],0) as Apr_21
            , coalesce([May-21],0) as May_21
            , coalesce([Jun-21],0) as Jun_21
            , coalesce([Jul-21],0) as Jul_21
            , coalesce([Aug-21],0) as Aug_21
            , coalesce([Sep-21],0) as Sep_21
            , coalesce([Oct-21],0) as Oct_21
            , coalesce([Nov-21],0) as Nov_21
            , coalesce([Dec-21],0) as Dec_21
            , null as total
            from (
                select format(sales_date, 'MMM-yy') as month, cast(replace(amount,'$','') as int) as amount
                from sales_data s
                ) as x
            pivot
            (
            sum(amount)
            for month in ([Jan-21], [Feb-21], [Mar-21], [Apr-21]
                            ,[May-21], [Jun-21] , [Jul-21], [Aug-21]
                            ,[Sep-21], [Oct-21] , [Nov-21], [Dec-21] )
            ) as y
    ) z;

