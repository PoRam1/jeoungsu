# 12세 이하인 여자 환자 목록 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132201
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:36:12

-- 코드를 입력하세요
SELECT
    PT_NAME,
    PT_NO,
    GEND_CD,
    AGE,
    case 
    when TLNO is null then 'NONE' 
    else TLNO 
    end as TLNO
from PATIENT 
where GEND_CD = 'W' and AGE<=12
order by AGE desc, PT_NAME asc