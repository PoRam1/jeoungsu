# 가까운 수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120890
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 18. 11:57:56

def solution(array, n):
    array.sort()
    
    answer = array[0]
    
    for i in array:
        if abs(i - n) < abs(answer - n):
            answer = i

    return answer