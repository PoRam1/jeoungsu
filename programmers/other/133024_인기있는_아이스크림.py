# 인기있는 아이스크림
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133024
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:36:22

-- 코드를 입력하세요
SELECT
    FLAVOR
from FIRST_HALF 
order by TOTAL_ORDER desc,
    SHIPMENT_ID