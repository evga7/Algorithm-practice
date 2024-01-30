import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
# map(int,input().split())
INF = sys.maxsize
N=int(input())
a=list(map(int,input().split()))
a.sort()
res=int(1e10)

l=0
mid=1
r=N-1
for i in range(N):
    left = i+1
    right = N - 1
    while left<right:
        s=a[i]+a[left]+a[right]
        if res>abs(s):
            res=abs(s)
            l=i
            mid=left
            r=right
        if s>=0:
            right-=1
        else:
            left+=1
print(a[l],a[mid],a[r])