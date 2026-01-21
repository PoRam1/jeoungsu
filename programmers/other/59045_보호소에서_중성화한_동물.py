# 보호소에서 중성화한 동물
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59045
# 작성자: 박정수
# 작성일: 2026. 01. 21. 09:35:32

-- 코드를 입력하세요
SELECT 
    i.ANIMAL_ID,
    i.ANIMAL_TYPE,
    i.NAME
from ANIMAL_INS i
join ANIMAL_OUTS o 
    on i.ANIMAL_ID = o.ANIMAL_ID
where i.SEX_UPON_INTAKE like '%Intact%' 
    and o.SEX_UPON_OUTCOME not like '%Intact%'
order by i.ANIMAL_ID;