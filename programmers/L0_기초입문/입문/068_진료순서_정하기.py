# 진료순서 정하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120835
# 알고리즘: 기초
# 작성자: 박정수
# 작성일: 2026. 06. 18. 11:28:53

def solution(emergency):
    answer = []

    sorted_emergency = sorted(emergency, reverse=True)

    for num in emergency:
        answer.append(sorted_emergency.index(num) + 1)

    return answer