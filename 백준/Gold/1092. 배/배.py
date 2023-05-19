import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
M=int(input())
b=list(map(int,input().split()))
b.sort(reverse=True)
a.sort(reverse=True)
if a[0]<b[0]:
    print(-1)
    exit(0)
res=0
cnt=0
chk=[0 for _ in range(M)]
while b:
    temp=a[:]
    for cur in temp:
        idx=0
        while b and b[idx]>cur and idx+1<len(b):
            idx+=1
        if b and b[idx]<=cur:
            del b[idx]
    res+=1
print(res)