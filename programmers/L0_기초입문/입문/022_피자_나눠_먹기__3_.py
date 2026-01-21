# 피자 나눠 먹기 (3)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 01. 21. 09:29:27

def solution(slice, n):
    answer = ((n-1) // slice) +1
    return answer