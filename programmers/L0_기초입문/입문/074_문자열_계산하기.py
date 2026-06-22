# 문자열 계산하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120902
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 22. 09:24:31

def solution(my_string):
    takens = my_string.split()
    answer = int(takens[0])
    
    for i in range(1 , len(takens), 2):
        operater = takens[i]
        number = int(takens[i + 1])
        
        if operater == '+' :
            answer += number
            
        else : 
            answer -= number
    
    
    
    return answer