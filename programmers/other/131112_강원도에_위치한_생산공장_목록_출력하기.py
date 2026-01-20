# 강원도에 위치한 생산공장 목록 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131112
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:32:21

-- 코드를 입력하세요
SELECT 
    FACTORY_ID,
    FACTORY_NAME,
    ADDRESS
from FOOD_FACTORY 
where ADDRESS like '%강원도%'
order by FACTORY_ID