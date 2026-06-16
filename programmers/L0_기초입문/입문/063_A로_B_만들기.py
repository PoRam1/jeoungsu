# A로 B 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120886
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 16. 11:47:02

def solution(before, after):
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0