# 문자열 정렬하기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120911
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 04. 09:17:33

def solution(my_string):
    my_string = my_string.lower()
    answer = sorted(my_string)
    return ''.join(answer)