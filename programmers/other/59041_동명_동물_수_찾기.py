# 동명 동물 수 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59041
# 작성자: 박정수
# 작성일: 2026. 02. 05. 09:18:10

select
    NAME,
    count(NAME) as COUNT
from
    ANIMAL_INS
where NAME is not null
group by NAME
having count >= 2
order by name;