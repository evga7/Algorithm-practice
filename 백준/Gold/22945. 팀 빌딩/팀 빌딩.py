import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
res=0
a=list(map(int,input().split()))
left=0
right=N-1
while left<right:
    res=max(res,(right-left-1)*min(a[right],a[left]))
    if a[left]<a[right]:
        left+=1
    else:
        right-=1
print(res)