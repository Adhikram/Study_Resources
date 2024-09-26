    with session_logs as (
        select 
            id,  
            onboarding_status,  
            is_visible,
            type,
            timestamp,
            lag(timestamp) over (partition by id, onboarding_status, is_visible, type order by timestamp) as session_change_start,
            lag(timestamp) over (partition by id order by timestamp) as prev_start
        from logs 
        group by id, onboarding_status, is_visible, type, timestamp
    ),
    session_start as (
        select 
            id,  
            onboarding_status,  
            is_visible,
            type,
            case 
                when session_change_start is null or session_change_start != prev_start 
                then timestamp 
                else null 
            end as begin_timestamp
        from session_logs
    )
    select 
        id,
        onboarding_status,
        is_visible,
        type,
        begin_timestamp, 
        lead(begin_timestamp) over (partition by id order by begin_timestamp) as end_timestamp 
    from session_start
    where begin_timestamp is not null;