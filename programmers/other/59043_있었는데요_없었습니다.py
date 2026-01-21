# 있었는데요 없었습니다
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59043
# 작성자: 박정수
# 작성일: 2026. 01. 21. 09:35:15

-- 코드를 입력하세요
SELECT 
    I.ANIMAL_ID,
    I.NAME
from ANIMAL_INS as I
join ANIMAL_OUTS as o
    on I.ANIMAL_ID = O.ANIMAL_ID
where I.DATETIME > O.DATETIME
order by I.DATETIME