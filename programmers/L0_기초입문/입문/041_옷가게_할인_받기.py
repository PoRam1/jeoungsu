# 옷가게 할인 받기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120818
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 04. 14. 09:05:27

def solution(price):
    if price >= 500000:
        answer = price * .80
    elif price >= 300000:
        answer = price * .90
    elif price >= 100000:
        answer = price * .95
    else:
        answer = price
    return int(answer)