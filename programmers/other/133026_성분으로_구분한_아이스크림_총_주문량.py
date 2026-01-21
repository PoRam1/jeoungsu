# 성분으로 구분한 아이스크림 총 주문량
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133026
# 작성자: 박정수
# 작성일: 2026. 01. 21. 09:39:40

SELECT 
    INGREDIENT_TYPE, 
    SUM(TOTAL_ORDER) TOTAL_ORDER
FROM FIRST_HALF F
JOIN ICECREAM_INFO I
    ON F.FLAVOR = I.FLAVOR
GROUP BY INGREDIENT_TYPE
ORDER BY TOTAL_ORDER ASC;