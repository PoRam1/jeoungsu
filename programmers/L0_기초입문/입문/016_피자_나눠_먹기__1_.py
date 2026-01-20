# 피자 나눠 먹기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120814
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 01. 20. 09:08:13

def solution(n):
    answer = 0
    if n % 7 == 0:
        answer = n / 7
    else :
        answer = n // 7 + 1
    return answer