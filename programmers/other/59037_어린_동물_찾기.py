# 어린 동물 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59037
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:28:54

-- 코드를 입력하세요
select 
    ANIMAL_ID,
    NAME
from ANIMAL_INS 
where INTAKE_CONDITION != 'Aged'