# 최솟값 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59038
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:28:46

-- 코드를 입력하세요
SELECT DATETIME as 시간
from ANIMAL_INS 
where DATETIME = (select min(DATETIME) from ANIMAL_INS )