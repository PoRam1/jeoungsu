# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 01. 22. 09:05:44

def solution(s1, s2):
    count = 0
    for i in s1:
        if i in s2:
            count += 1
    return count