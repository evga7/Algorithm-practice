import sys
def input():return sys.stdin.readline().rstrip()
res_v=[0 for _ in range(26)]
s=input()
for cur in s:
    res_v[ord(cur)-ord('A')]+=1
N=int(input())
b=[]
res=987654321
v=[0 for _ in range(N)]
for i in range(N):
    a=input().split()
    b.append((int(a[0]),a[1]))
def go(cnt,mo):
    if cnt==N:
        f=0
        for cur in s:
            if res_v[ord(cur) - ord('A')] > 0:
                f = 1
                break
        if not f:
            global res
            res=min(res,mo)
        return
    go(cnt+1,mo)
    for cur in b[cnt][1]:
        res_v[ord(cur)-ord('A')]-=1
    go(cnt+1,mo+b[cnt][0])
    for cur in b[cnt][1]:
        res_v[ord(cur)-ord('A')]+=1
go(0,0)
if res==987654321:
    res=-1
print(res)