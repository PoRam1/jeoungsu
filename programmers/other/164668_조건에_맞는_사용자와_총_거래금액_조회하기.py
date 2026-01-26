# 조건에 맞는 사용자와 총 거래금액 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164668
# 작성자: 박정수
# 작성일: 2026. 01. 26. 09:45:07

-- 코드를 입력하세요
SELECT 
    b.WRITER_ID,
    u.NICKNAME,
    sum(PRICE) as TOTAL_SALES
from USED_GOODS_BOARD as b
left join USED_GOODS_USER as u
    on b.WRITER_ID = u.USER_ID
where STATUS = 'DONE'
group by NICKNAME
having TOTAL_SALES >= '700000'
order by TOTAL_SALES

    