# Write your MySQL query statement below
SELECT w.name as warehouse_name, SUM(w.units * (p.width * p.Length * p.Height))as volume
from Warehouse w, Products p
WHERE w.product_id = p.product_id
group by w.name
