# 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/151137
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:45:39

-- 코드를 입력하세요
SELECT 
    CAR_TYPE,
    count(1) as "CARS"
from CAR_RENTAL_COMPANY_CAR 
where  options like "%통풍시트%"or options like "%열선시트%"or options like "%가죽시트%"
group by CAR_TYPE
order by CAR_TYPE;