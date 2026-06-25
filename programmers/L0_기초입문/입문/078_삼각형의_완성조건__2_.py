# 삼각형의 완성조건 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120868
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 25. 09:10:35

def solution(sides):
    answer = 0
    
    for x in range(1,sum(sides)):
        triangle = sorted(sides +[x])
        
        if triangle[0] + triangle[1] >triangle[2]:
            answer += 1
        
        
        
        
    return answer