import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
col=[0 for _ in range(N+1)]
res=0
def chk(cnt):
    for i in range(cnt):
        if col[i]==col[cnt] or abs(col[i]-col[cnt])==abs(i-cnt):
            return False
    return True
def go(cnt):
    if cnt==N:
        global res
        res+=1
        return
    for i in range(N):
        col[cnt]=i
        if chk(cnt):
            go(cnt+1)
go(0)
print(res)