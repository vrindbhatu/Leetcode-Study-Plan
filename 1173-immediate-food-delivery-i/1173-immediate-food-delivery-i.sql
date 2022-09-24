# Write your MySQL query statement below

SELECT
ROUND((Select count(*) FROM Delivery WHERE order_date = customer_pref_delivery_date) * 100/ COUNT(*),2) AS immediate_percentage
FROM Delivery
