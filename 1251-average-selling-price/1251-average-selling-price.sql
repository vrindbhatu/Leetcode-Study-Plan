# Write your MySQL query statement below

SELECT p.product_id, ROUND(SUM(p.price *u.units)/ SUM(u.units),2)as average_price
from Prices p, UnitsSold u
where p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_Date
GROUP BY product_id
