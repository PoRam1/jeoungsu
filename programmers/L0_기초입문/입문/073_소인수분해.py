# 소인수분해
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120852
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 19. 19:33:41

def solution(n):
    answer = []
    
    for num in range(2,n+1):
        if n % num == 0:
            answer.append(num)

            while n % num == 0:
                n //= num

    return answer   
    