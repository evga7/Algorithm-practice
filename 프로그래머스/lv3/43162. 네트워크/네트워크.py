p=[i for i in range(201)]
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

def solution(n, computers):
    answer = n
    for i in range(len(computers)):
        for j in range(i+1,n):
            if computers[i][j]:
                if u(i+1,j+1):
                    answer-=1
    return answer