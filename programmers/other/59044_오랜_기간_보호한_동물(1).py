# 오랜 기간 보호한 동물(1)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59044
# 작성자: 박정수
# 작성일: 2026. 01. 26. 09:26:25

-- 코드를 입력하세요
SELECT 
    i.NAME,
    i.DATETIME
from ANIMAL_INS i
left join 
    ANIMAL_OUTS o on i.ANIMAL_ID =o.ANIMAL_ID
where o.ANIMAL_ID is null
order by DATETIME
limit 3
