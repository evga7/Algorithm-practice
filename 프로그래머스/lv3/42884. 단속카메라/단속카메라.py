def solution(routes):
    answer = 0
    q=[]
    routes.sort(key=lambda x:x[1])
    for cur in routes:
        s=cur[0]
        e=cur[1]
        if q and q[-1]>=s:continue
        q.append(e)
    return len(q)