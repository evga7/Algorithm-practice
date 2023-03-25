def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    b=-30001
    for cur in routes:
        s=cur[0]
        e=cur[1]
        if b>=s:continue
        answer+=1
        b=e
    return answer