p=[i for i in range(101)]
def f(x):
    if x==p[x]:
        return x
    p[x]=f(p[x])
    return p[x]
def u(x,y):
    x=f(x)
    y=f(y)
    if x!=y:
        p[y]=x
        return True
    return False
def solution(n, costs):
    answer = 0
    c=sorted(costs,key=lambda x:x[2])
    for cur in c:
        x,y,co=cur[0],cur[1],cur[2]
        if u(x,y):
            answer+=co
    return answer