# 루시와 엘라 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59046
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:36:32

-- 코드를 입력하세요
SELECT 
    ANIMAL_ID,
    NAME,
    SEX_UPON_INTAKE
from ANIMAL_INS
where NAME in('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')