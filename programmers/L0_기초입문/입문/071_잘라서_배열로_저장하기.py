# 잘라서 배열로 저장하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120913
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 18. 12:27:02

def solution(my_str, n):
    answer = []
    
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
        
    return answer