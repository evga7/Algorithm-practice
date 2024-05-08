def solution(n, m, section):
    answer = 0
    back=0
    for cur in section:
        if back<cur:
            back=cur+m-1
            answer+=1
    return answer