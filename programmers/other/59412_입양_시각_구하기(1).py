# 입양 시각 구하기(1)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59412
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:38:31

-- 코드를 입력하세요
SELECT 
    Hour(DATETIME) as hour,
    count(*) as count
from ANIMAL_OUTS 
where hour(DATETIME) between 9 and 20
group by hour
order by hour