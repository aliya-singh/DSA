# Write your MySQL query statement below
select W1.id from Weather as W1 join Weather as W2 where datediff(W1.recordDate, W2.recordDate) = 1 and w1.temperature > w2.temperature