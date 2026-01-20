# 평균 일일 대여 요금 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/151136
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:36:55

-- 코드를 입력하세요
SELECT round(avg(DAILY_FEE)) as AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR 
where car_type = 'SUV'