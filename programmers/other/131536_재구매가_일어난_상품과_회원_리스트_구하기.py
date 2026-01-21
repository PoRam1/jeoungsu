# 재구매가 일어난 상품과 회원 리스트 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131536
# 작성자: 박정수
# 작성일: 2026. 01. 21. 09:43:55

-- 코드를 입력하세요
SELECT 
    USER_ID,
    PRODUCT_ID
from ONLINE_SALE o
group by 
    USER_ID,
    PRODUCT_ID
having COUNT(*) >= 2
ORDER BY USER_ID ASC, PRODUCT_ID DESC;