import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
a=list(map(int,input().split()))
M=int(input())
a.sort()
left=0
right=N-1
s=0
res=0
while left<right:
    s=a[left]+a[right]
    if s>=M:
        if s==M:
            res+=1
        right-=1
    else:
        left+=1
print(res)