# Write your MySQL query statement below
# Select seller_name as SELLER_NAME
# from Seller s LEFT JOIN Orders o
# ON s.seller_id = o.seller_id and YEAR(o.sale_date) = "2020"
# WHere o.seller_id is NULL
# order by seller_name


# select seller_name as SELLER_NAME
# from Seller
# where seller_id not in
# (select distinct(seller_id) from Orders where year(sale_date) = "2020")
# order by seller_name



select seller_name as SELLER_NAME
from Seller
where seller_id not in (select seller_id from Orders where Year(sale_date) = 2020)
order by seller_name