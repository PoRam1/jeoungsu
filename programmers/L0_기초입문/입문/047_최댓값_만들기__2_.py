# 최댓값 만들기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120862
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 01. 14:01:24

def solution(numbers):
    numbers.sort()
    
    negative_max = numbers[0]*numbers[1]
    positive_max = numbers[-1]* numbers[-2]
    
    if negative_max > positive_max:
        return negative_max
    else:
        return positive_max
        
    