# 짝수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 01. 19. 09:24:58

def solution(n):
    answer = 0
    for i in range(0, n+1, 2):
        answer += i
    return answer