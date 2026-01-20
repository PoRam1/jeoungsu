# DATETIME에서 DATE로 형 변환
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59414
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:32:28

-- 코드를 입력하세요
SELECT 
    ANIMAL_ID,
    NAME,
    DATE_FORMAT(DATETIME, '%Y-%m-%d') as'날짜'
from ANIMAL_INS
order by ANIMAL_ID