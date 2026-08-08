# Write your MySQL query statement below
Select firstName ,lastName ,city,state 
FROM person p 
left Join Address a on  p.personId =a.personId    

