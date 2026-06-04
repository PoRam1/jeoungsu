# 대문자와 소문자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120893
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 04. 09:29:48

def solution(my_string):
    answer = ""

    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()

    return answer