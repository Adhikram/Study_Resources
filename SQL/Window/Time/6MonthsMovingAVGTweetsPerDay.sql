-- 6 months moving average of tweets per day.
select dte,
    tweet_millions,
    avg(tweet_millions) over(
        order by dte range between interval '6' month preceding
            and current row
    ) as average
from tweets;
-- Output
-- dte        tweet_millions  average
-- 2019-01-01 0.1             0.1
-- 2019-02-01 0.2             0.15
-- 2019-03-01 0.3             0.2
-- 2019-04-01 0.4             0.25
-- 2019-05-01 0.5             0.3