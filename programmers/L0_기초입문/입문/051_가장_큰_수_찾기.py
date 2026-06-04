# 가장 큰 수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120899
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 04. 09:15:59

def solution(array):
    max_num = max(array)
    max_index = array.index(max_num)

    return [max_num, max_index]