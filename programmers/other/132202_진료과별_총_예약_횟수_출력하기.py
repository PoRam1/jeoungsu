# 진료과별 총 예약 횟수 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132202
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:42:56

-- 코드를 입력하세요
SELECT  
    MCDP_CD as "진료과코드",
    count(1) as "5월예약건수"
from APPOINTMENT 
where MONTH(APNT_YMD) = '5'
group by MCDP_CD
order by count(1), MCDP_CD