# 숨어있는 숫자의 덧셈 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120851
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 02. 05. 09:14:29

def solution(my_string):
    answer = 0
    number = ['1','2','3','4','5','6','7','8','9']
    for i in my_string:
        if i in number:
            answer += int(i)
    return answer