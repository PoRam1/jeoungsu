# 합성수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120846
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 04. 12:11:20

def solution(n):
    answer = 0
    for num in range(1 , n+1):
        count = 0
        
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count >= 3:
            answer += 1
    return answer