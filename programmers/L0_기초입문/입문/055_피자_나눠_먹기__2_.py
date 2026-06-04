# 피자 나눠 먹기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120815
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 04. 09:38:34

def solution(n):
    pizza = 1

    while True:
        if (pizza * 6) % n == 0:
            return pizza
        
        pizza += 1