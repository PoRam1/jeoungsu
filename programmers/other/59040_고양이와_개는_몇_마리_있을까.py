# 고양이와 개는 몇 마리 있을까
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59040
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:38:20

-- 코드를 입력하세요
SELECT 
    ANIMAL_TYPE,
    count(*) as count
from ANIMAL_INS
group by ANIMAL_TYPE
order by ANIMAL_TYPE