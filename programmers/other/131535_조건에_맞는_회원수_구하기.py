# 조건에 맞는 회원수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131535
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:34:49

-- 코드를 입력하세요
SELECT 
    count(*) as USRS
from USER_INFO 
where YEAR(JOINED) = 2021 and AGE between 20 and 29