# 중복된 문자 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120888
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 16. 11:19:25

def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer
