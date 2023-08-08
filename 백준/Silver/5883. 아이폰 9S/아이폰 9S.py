import sys
def input():return sys.stdin.readline().rstrip()
prime=[0 for _ in range(10001)]
INF=sys.maxsize
N=int(input())
a=[int(input()) for _ in range(N)]
st=set(a)
res=1
for cur in st:
    cnt=1
    back=a[0]
    for i in range(1,N):
        if a[i]==cur:continue
        if a[i]==back:
            cnt+=1
            res=max(res,cnt)
        else:
            cnt=1
        back=a[i]
print(res)