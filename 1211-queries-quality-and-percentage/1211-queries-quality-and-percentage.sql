# Write your MySQL query statement below

# SELECT query_name,
# ROUND(AVG(rating/position),2) AS quality,
# ROUND(SUM((IF(rating < 3,1,0))) * 100 /COUNT(*) ,2) AS poor_query_percentage
# FROM Queries
# GROUP BY query_name

select query_name, round(avg(rating/position),2) as quality,
round(count((if (rating< 3,1,null))) * 100/count(*),2) as poor_query_percentage
from queries
group by query_name
