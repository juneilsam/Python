# 체육복

def solution(n, lost, reserve):
    answer = 0
    a = set(lost) - set(reserve)
    b = set(reserve) - set(lost)
    answer = n - len(a)
    c = list(reversed([i for i in a]))
    for i in c:
        if i+1 in b:
            answer += 1
            b.remove(i+1)
        elif i-1 in b:
            answer += 1
            b.remove(i-1)
    return answer
