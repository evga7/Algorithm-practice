import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
res=0
v=[0 for _ in range(N)]
def go(idx):
    cnt=0
    for cur in a:
        if cur[0]<=0:
            cnt+=1
    global res
    res=max(res,cnt)
    if idx==N or cnt==N:
        return
    S,W=a[idx][0],a[idx][1]
    if S<=0:
        go(idx+1)
    for i in range(N):
        if i==idx:continue
        s,w=a[i][0],a[i][1]
        if S>0 and s>0:
            a[i][0]-=W
            a[idx][0]-=w
            go(idx+1)
            a[idx][0]+=w
            a[i][0]+=W

go(0)
print(res)