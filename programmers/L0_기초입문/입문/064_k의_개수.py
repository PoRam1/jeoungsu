# k의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120887
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 16. 12:15:23

def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        answer += str(num).count(str(k))
        
    return answer

