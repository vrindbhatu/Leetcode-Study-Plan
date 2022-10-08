# Write your MySQL query statement below





with highest_salary as (
select name, departmentId, salary, RANK() OVER(PARTITION BY departmentId order by salary desc) as highest_rank
from Employee
)

select d.name as Department, h.name as Employee, h.salary
from highest_salary h, Department d
where d.id = h.departmentId
and highest_rank = 1

# select * from highest_salary


# WITH salaries_ranked AS (
#     SELECT
#         e.departmentId id,
#         e.name name,
#         e.salary salary,
#         RANK() OVER(
#             PARTITION BY e.departmentId
#             ORDER BY e.salary DESC
#         ) srank
#     FROM Employee e
# )
# SELECT
#     d.name Department,
#     sr.name Employee,
#     sr.salary
# FROM salaries_ranked sr
# JOIN Department d ON d.id = sr.id
# WHERE sr.srank = 1;