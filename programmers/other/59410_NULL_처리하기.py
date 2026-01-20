# NULL 처리하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59410
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:32:06

-- 코드를 입력하세요
SELECT 
    ANIMAL_TYPE,
    ifnull(name, 'No name') as name,
    SEX_UPON_INTAKE
from ANIMAL_INS