# 7의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120912
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 17. 20:02:11

def solution(array):
    answer = 0

    for num in array:
        answer += str(num).count('7')

    return answer