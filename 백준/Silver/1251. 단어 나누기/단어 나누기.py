import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
s=input()
v=[]
l=len(s)
res="z"*51
def go(idx,ss,cnt):
    if cnt==3:
        if idx!=l:
            return
    if idx==l:
        if cnt==3:
            temp=""
            for cur in v:
                temp+=cur[::-1]
            global res
            res=min(res,temp)
        return
    go(idx+1,ss+s[idx],cnt)
    v.append(ss+s[idx])
    go(idx + 1, "", cnt+1)
    v.pop()
go(0,"",0)
print(res)