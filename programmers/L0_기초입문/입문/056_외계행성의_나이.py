# 외계행성의 나이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120834
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 04. 09:42:25

def solution(age):
    alphabet = "abcdefghij"
    answer = ""

    for i in str(age):
        answer += alphabet[int(i)]

    return answer