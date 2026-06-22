# 영어가 싫어요
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120894
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 22. 19:20:45

def solution(numbers):
    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(10):
        numbers = numbers.replace(word[i], str(i))
        
    return int(numbers)