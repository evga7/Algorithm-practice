import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
arr.sort()
lm=0
rm=0
res=0
l=arr[N-1][0]
a=[0 for _ in range(l+2)]
for cur in arr:
    a[cur[0]]=cur[1]
for i in range(l+1):
    lm=max(lm,a[i])
    rm=max(a[i:])
    if rm<=a[i]>=lm:
        res+=lm
    else:
        res += min(lm, rm)
print(res)