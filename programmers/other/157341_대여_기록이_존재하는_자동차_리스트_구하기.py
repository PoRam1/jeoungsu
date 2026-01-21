# 대여 기록이 존재하는 자동차 리스트 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/157341
# 작성자: 박정수
# 작성일: 2026. 01. 21. 09:43:23

-- 코드를 입력하세요
SELECT 
    distinct(c.CAR_ID)
from CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_RENTAL_HISTORY r
    on c.CAR_ID = r.CAR_ID
where c.CAR_TYPE = "세단" and MONTH(START_DATE) = 10
order by CAR_ID desc