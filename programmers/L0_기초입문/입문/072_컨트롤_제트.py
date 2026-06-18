# 컨트롤 제트
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120853
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 18. 12:44:04

def solution(s):
    stack =[]
    
    for i in s.split():
        if i == 'Z':
            stack.pop()
        else:
            stack.append(int(i))
    
    return sum(stack)
        
