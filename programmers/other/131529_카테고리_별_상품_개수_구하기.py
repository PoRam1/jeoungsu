# 카테고리 별 상품 개수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131529
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:38:03

-- 코드를 입력하세요
SELECT 
    substr(PRODUCT_CODE, 1, 2) as CATEGORY,
    count(*) as PRODUCTS
from PRODUCT
group by CATEGORY
order by CATEGORY;