# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 01. 30. 09:14:03

def solution(my_string):
    problem = ['a', 'e', 'i', 'o', 'u']
    for i in problem:
        my_string = my_string.replace(i, "")
    return my_string