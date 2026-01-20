# 경기도에 위치한 식품창고 목록 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131114
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:32:14

-- 코드를 입력하세요
SELECT 
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    case when FREEZER_YN is null then 'N'
    else FREEZER_YN end as FREEZER_YN
from FOOD_WAREHOUSE
where ADDRESS like '경기도%'