# 오랜 기간 보호한 동물(2)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59411
# 작성자: 박정수
# 작성일: 2026. 01. 21. 09:35:23

select 
    i.ANIMAL_ID,
    i.NAME
from ANIMAL_INS as i
left join ANIMAL_OUTS as o
    on i.ANIMAL_ID = o.ANIMAL_ID
where o.ANIMAL_ID is not null
order by timestampdiff (DAY, i.DATETIME ,o.DATETIME) desc
limit 2