# 배열 회전시키기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120844
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 04. 11:11:20

def solution(numbers, direction):
    if direction == "right":
        return [numbers[-1]] + numbers[:-1]
    else:
        return numbers[1:] + [numbers[0]]