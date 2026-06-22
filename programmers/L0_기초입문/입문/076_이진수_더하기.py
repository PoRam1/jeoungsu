# 이진수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120885
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 22. 19:13:54

def solution(bin1, bin2):
    number1 = int(bin1, 2)
    number2 = int(bin2, 2)
    
    answer = bin(number1 + number2)[2:]
    return answer