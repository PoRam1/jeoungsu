# 흉부외과 또는 일반외과 의사 목록 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132203
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:34:08

select 
    DR_NAME,
    DR_ID,
    MCDP_CD,
    DATE_FORMAT (HIRE_YMD, '%Y-%m-%d') as HIRE_YMD
from DOCTOR 
where MCDP_CD in ('CS', 'GS')
order by HIRE_YMD desc , DR_NAME