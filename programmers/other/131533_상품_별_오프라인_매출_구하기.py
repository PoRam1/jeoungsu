# 상품 별 오프라인 매출 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131533
# 작성자: 박정수
# 작성일: 2026. 01. 21. 09:35:04

-- 코드를 입력하세요
SELECT 
    P.PRODUCT_CODE,
    sum(O.SALES_AMOUNT*P.PRICE) as SALES
from PRODUCT as P
join OFFLINE_SALE as O 
    on P.PRODUCT_ID = O.PRODUCT_ID
group by PRODUCT_CODE
order by SALES DESC, PRODUCT_CODE