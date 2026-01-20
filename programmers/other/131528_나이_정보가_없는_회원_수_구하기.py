# 나이 정보가 없는 회원 수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131528
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:30:17

-- 코드를 입력하세요
SELECT
    Count(USER_ID) as USERS
from USER_INFO 
where AGE is null