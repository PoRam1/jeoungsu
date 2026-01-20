# 동명 동물 수 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59041
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:37:54

-- 코드를 입력하세요
SELECT 
    NAME,
    count(name) as count
from ANIMAL_INS
group by NAME
having  count(name) >=2
order by name