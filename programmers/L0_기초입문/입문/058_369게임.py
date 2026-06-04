# 369게임
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120891
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 04. 11:21:09

def solution(order):
    answer = 0
    for i in str(order):
        if i == "3" or  i == "6" or i == "9":
            answer += 1
    return answer