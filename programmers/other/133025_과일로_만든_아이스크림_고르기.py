# 과일로 만든 아이스크림 고르기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133025
# 작성자: 박정수
# 작성일: 2026. 01. 21. 09:43:45

-- 코드를 입력하세요
SELECT f.FLAVOR
from FIRST_HALF f
join ICECREAM_INFO i 
    on f.FLAVOR = i.FLAVOR
where f.TOTAL_ORDER > 3000 and INGREDIENT_TYPE = "fruit_based"
order by f.TOTAL_ORDER desc