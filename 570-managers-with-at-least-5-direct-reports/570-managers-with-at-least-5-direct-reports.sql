# Write your MySQL query statement below


select e.name
from
Employee e, Employee m
WHERE e.id = m.managerId
group by m.managerId
having count(*) >=5
