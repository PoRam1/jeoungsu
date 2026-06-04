# 숫자 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 04. 09:20:07

def solution(num, k):
    num = str(num)
    k = str(k)

    if k in num:
        return num.index(k) + 1
    else:
        return -1