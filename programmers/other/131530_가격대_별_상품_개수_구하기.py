# 가격대 별 상품 개수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131530
# 작성자: 박정수
# 작성일: 2026. 01. 21. 09:43:11

-- 코드를 입력하세요
SELECT 
    floor(PRICE / 10000) *10000 as PRICE_GROUP,
    count(PRODUCT_CODE) as PRODUCTS
from PRODUCT
group by floor(PRICE / 10000) *10000
order by PRICE_GROUP asc