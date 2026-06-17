# 숨어있는 숫자의 덧셈 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120864
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 17. 17:32:15

def solution(my_string):
    answer = 0
    num = ''

    for char in my_string:
        if char.isdigit():
            num += char
        else:
            if num != '':
                answer += int(num)
                num = ''

    if num != '':
        answer += int(num)

    return answer
            

            