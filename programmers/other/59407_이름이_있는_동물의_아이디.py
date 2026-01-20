# 이름이 있는 동물의 아이디
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59407
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:27:11

-- 코드를 입력하세요
SELECT  ANIMAL_ID
from animal_ins
where name is not null
order by ANIMAL_ID asc