# 공 던지기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120843
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 22. 18:25:53

def solution(numbers, k):
    
    index = (k-1) * 2 % len(numbers)
    answer = numbers[index]
    return answer