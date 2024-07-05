import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N,M=map(int,input().split())
a=[list(input().split()) for _ in range(N)]
res=987654321
mx=0
def chk(s):
    cnt=0
    for cur in s:
        if cur=='Y':
            cnt+=1
    return cnt
def go(idx,s,cnt):
    global res,mx
    ch=chk(s)
    if ch and ch>=mx:
        if ch>mx:
            res=987654321
            mx=ch
        res=min(res,cnt)
    if idx==N:
        return
    go(idx+1,s,cnt)
    temp=""
    for i,cur in enumerate(a[idx][1]):
        if cur=='Y' or s[i]=='Y':
            temp+='Y'
        else:
            temp+='N'
    go(idx+1,temp,cnt+1)
go(0,"N"*M,0)
if res==987654321:
    res=-1
print(res)