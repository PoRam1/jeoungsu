# 자릿수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 02. 02. 09:46:13

def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer += int(i)
    return answer