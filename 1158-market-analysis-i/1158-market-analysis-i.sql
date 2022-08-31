# Write your MySQL query statement below
Select u.user_id as buyer_id, u.join_date, COUNT(o.order_id) AS orders_in_2019
FROM Users u LEFT JOIN Orders o
ON u.user_id = o.buyer_id AND YEAR(o.order_Date) = '2019'
GROUP BY u.user_id

