# 카테고리 별 도서 판매량 집계하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/144855
# 작성자: 박정수
# 작성일: 2026. 01. 21. 09:34:52

-- 코드를 입력하세요
SELECT
    CATEGORY,
    sum(sales) as TOTAL_SALES
from BOOK B
join BOOK_SALES s
    on B.BOOK_ID = S.BOOK_ID
where SALES_DATE like '2022-01%'
group by CATEGORY
order by CATEGORY;