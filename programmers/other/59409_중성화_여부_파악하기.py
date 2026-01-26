# 중성화 여부 파악하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59409
# 작성자: 박정수
# 작성일: 2026. 01. 26. 09:21:17

-- 코드를 입력하세요
SELECT 
   ANIMAL_ID,
   NAME,
   case
   when SEX_UPON_INTAKE like '%Neutered%' or SEX_UPON_INTAKE like '%Spayed%' then 'O'
   else 'X' end as 중성화
 from ANIMAL_INS 
 order by ANIMAL_ID