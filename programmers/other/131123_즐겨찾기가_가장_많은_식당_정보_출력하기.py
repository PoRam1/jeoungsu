# 즐겨찾기가 가장 많은 식당 정보 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131123
# 작성자: 박정수
# 작성일: 2026. 02. 04. 09:18:19

-- 코드를 입력하세요
SELECT 
    FOOD_TYPE,
    REST_ID,
    REST_NAME,
    FAVORITES
from (
    select 
    FOOD_TYPE,
    REST_ID,
    REST_NAME,
    FAVORITES,
    ROW_NUMBER() over(
        partition by FOOD_TYPE
        order by FAVORITES desc) as rn
    from
    REST_INFO
    ) ranked
where rn = 1
order by FOOD_TYPE desc;
