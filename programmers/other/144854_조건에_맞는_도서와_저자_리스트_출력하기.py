# 조건에 맞는 도서와 저자 리스트 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/144854
# 작성자: 박정수
# 작성일: 2026. 01. 21. 09:38:54

-- 코드를 입력하세요
select
    b.BOOK_ID,
    a.AUTHOR_NAME,
    DATE_FORMAT(published_date, '%Y-%m-%d') published_date
from BOOK b 
join AUTHOR a
    on b.AUTHOR_ID = a.AUTHOR_ID
where b.CATEGORY = "경제"
order by PUBLISHED_DATE