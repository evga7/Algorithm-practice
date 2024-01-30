import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
# map(int,input().split())
INF = sys.maxsize
N=int(input())
a=list(map(int,input().split()))
a.sort()
res=int(1e10)
left=0
right=N-1
l=0
r=N-1
while left<right:
    s=a[left]+a[right]
    if res>abs(s):
        res=abs(s)
        l=left
        r=right
    if s>=0:
        right-=1
    else:
        left+=1
print(a[l],a[r])
