v=[0 for _ in range(9)]
res=0
def go(hp,cnt,d,l):
    global res
    res=max(res,cnt)
    for i in range(l):
        a,b=d[i][0],d[i][1]
        if not v[i] and a<=hp:
            v[i]=1
            go(hp-b,cnt+1,d,l)
            v[i]=0
    
def solution(k, dungeons):
    go(k,0,dungeons,len(dungeons))
    return res