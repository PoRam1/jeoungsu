# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 04. 14. 09:24:46

def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)