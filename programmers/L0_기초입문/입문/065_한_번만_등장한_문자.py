# 한 번만 등장한 문자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120896
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 16. 12:31:22

def solution(s):
    answer = ''

    for char in s:
        if s.count(char) == 1:
            answer += char

    return ''.join(sorted(answer))