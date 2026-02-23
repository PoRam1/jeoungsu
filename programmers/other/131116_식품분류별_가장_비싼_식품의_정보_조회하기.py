# 식품분류별 가장 비싼 식품의 정보 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131116
# 작성자: 박정수
# 작성일: 2026. 02. 23. 09:31:04

SELECT 
    CATEGORY,
    price,
    PRODUCT_NAME
from (
    select 
        CATEGORY,
        price,
        PRODUCT_NAME,
        row_number() over (partition by CATEGORY order by price desc) as rn
    from FOOD_PRODUCT 
    where CATEGORY in ('과자','국','김치','식용유')
) f
where rn = 1
order by price desc