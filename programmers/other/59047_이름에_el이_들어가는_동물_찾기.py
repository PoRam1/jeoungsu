# 이름에 el이 들어가는 동물 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59047
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:29:09

-- 코드를 입력하세요
SELECT 
    ANIMAL_ID,
    NAME
from ANIMAL_INS 
where ANIMAL_TYPE= 'Dog' and NAME like '%el%'
order by NAME asc