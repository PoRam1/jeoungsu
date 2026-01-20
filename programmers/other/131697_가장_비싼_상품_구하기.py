# 가장 비싼 상품 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131697
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:31:17

-- 코드를 입력하세요
SELECT price as MAX_PRICE
from PRODUCT
where price = (select MAX(PRICE) from PRODUCT )