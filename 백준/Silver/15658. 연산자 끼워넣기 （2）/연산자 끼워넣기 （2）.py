import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N = int(input())
a=list(map(int,input().split()))
P,S,M,SU=map(int,input().split())
res1=-9876543210
res2=9876543210
def go(idx,p,s,m,su,SS):
    if idx==N:
        global res1, res2
        res1 = max(res1, SS)
        res2 = min(res2, SS)
        return

    if s:
        go(idx+1,p,s-1,m,su,SS-a[idx])
    if su:
        go(idx+1,p,s,m,su-1,int(SS/a[idx]))
    if p:
        go(idx+1,p-1,s,m,su,SS+a[idx])
    if m:
        go(idx+1,p,s,m-1,su,SS*a[idx])

go(1,P,S,M,SU,a[0])
print(res1)
print(res2)