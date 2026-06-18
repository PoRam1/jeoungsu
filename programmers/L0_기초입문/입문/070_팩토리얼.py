# 팩토리얼
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120848
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 18. 12:23:14

def solution(n):
    factorial = 1
    i = 1
    
    while factorial <= n:
        i += 1
        factorial *= i

    return i - 1