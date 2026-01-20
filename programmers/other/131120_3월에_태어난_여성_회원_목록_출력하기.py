# 3월에 태어난 여성 회원 목록 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131120
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:37:05

-- 코드를 입력하세요
SELECT
    MEMBER_ID,
    MEMBER_NAME,
    GENDER,
    DATE_FORMAT (DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE 
where 
    GENDER = "W" 
    and MONTH(DATE_OF_BIRTH) = 3
    and TLNO is not null