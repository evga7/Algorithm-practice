import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=list(map(int,input().split()))
left=0
right=N-1
s=int(1e9)
while left<right:
    ss=a[left]+a[right]
    if abs(s)>abs(ss):
        s=ss
    if ss>=0:
        right-=1
    else:
        left+=1
print(s)