# 조건에 맞는 도서 리스트 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/144853
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:36:41

-- 코드를 입력하세요
SELECT 
    BOOK_ID,
    DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from BOOK 
where PUBLISHED_DATE like '2021%' and CATEGORY = "인문"