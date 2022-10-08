# Write your MySQL query statement below
# select 
# case
#     when count(*) = 1 then num
#     else null
# end as num
# from MyNumbers
# group by num
# order by num desc
# limit 1



select if(count(*) =1, num,null) as num
from MyNumbers
group by num
order by num desc
limit 1

