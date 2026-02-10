# 조건에 부합하는 중고거래 댓글 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164673
# 작성자: 박정수
# 작성일: 2026. 02. 10. 09:17:43

-- 코드를 입력하세요
SELECT 
    b.TITLE,
    b.BOARD_ID,
    r.REPLY_ID,
    r.WRITER_ID,
    r.CONTENTS,
    date_format(r.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD b
join USED_GOODS_REPLY r
    on b.BOARD_ID = r.BOARD_ID
where
    YEAR(b.CREATED_DATE) =2022 and
    MONTH(b.CREATED_DATE) = 10
order by r.CREATED_DATE asc , b.TITLE asc

    