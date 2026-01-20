# 가격이 제일 비싼 식품의 정보 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131115
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:34:19

-- 코드를 입력하세요
SELECT
    PRODUCT_ID,
    PRODUCT_NAME,
    PRODUCT_CD,
    CATEGORY,
    PRICE
from FOOD_PRODUCT 
where price = (select max(PRICE) from FOOD_PRODUCT)