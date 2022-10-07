# Write your MySQL query statement below
SELECT sale_date,  SUM(CASE WHEN fruit = "apples" then sold_num end) - SUM(CASE WHEN fruit = "oranges" then sold_num end) as diff
from Sales
group by sale_date
order by sale_date
