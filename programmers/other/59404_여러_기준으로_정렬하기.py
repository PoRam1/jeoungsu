# 여러 기준으로 정렬하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59404
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:29:00

-- 코드를 입력하세요
SELECT
    ANIMAL_ID,
    NAME,
    DATETIME
from ANIMAL_INS
order by NAME asc, DATETIME desc