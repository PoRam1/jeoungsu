# 조건에 부합하는 중고거래 상태 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164672
# 작성자: 박정수
# 작성일: 2026. 02. 10. 09:00:47

-- 코드를 입력하세요
SELECT 
    BOARD_ID,
    WRITER_ID,
    TITLE,
    PRICE,
    case when STATUS = 'DONE' then '거래완료'
    when STATUS = 'RESERVED' then '예약중'
    when STATUS = 'SALE' then '판매중'
    end AS STATUS
from USED_GOODS_BOARD
where DATE_format(CREATED_DATE,'%Y-%m-%d') = '2022-10-05'
order by BOARD_ID desc