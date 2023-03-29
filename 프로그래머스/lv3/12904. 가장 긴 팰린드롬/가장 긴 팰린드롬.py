import sys
sys.setrecursionlimit(10 ** 6)
d=[[-1 for _ in range(2501)] for _ in range(2501)]
def g(a,b,s):
    if a>=b:
        return 1
    if d[a][b]!=-1:
        return d[a][b]
    ret=0
    if s[a]==s[b]:
        ret=g(a+1,b-1,s)
    d[a][b]=ret
    return d[a][b]
def solution(s):
    answer = 1
    l=len(s)
    for i in range(l):
        for j in range(i+1,l):
            if g(i,j,s):
                answer=max(abs(i-j)+1,answer)
    return answer