# Write your MySQL query statement below
WITH cte as
(SELECT *
FROM Sales
ORDER BY sale_date),

cte2 as
(SELECT *, LEAD(sold_num,1) OVER(PARTITION BY sale_date) as orange_sold
FROM cte)

SELECT sale_date, (sold_num - orange_sold) as diff
FROM  cte2
WHERE orange_sold is not null
ORDER BY sale_date
    