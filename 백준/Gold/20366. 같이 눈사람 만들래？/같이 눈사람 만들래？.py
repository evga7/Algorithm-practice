import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
# map(int,input().split())
INF = sys.maxsize
N=int(input())
a=list(map(int,input().split()))
a.sort()
res=int(1e10)
for i in range(N):
    for j in range(i+3,N):
        left=i+1
        right=j-1
        while left<right:
            s=(a[i]+a[j])-(a[left]+a[right])
            if res>abs(s):
                res=abs(s)
            if s<0:
                right-=1
            else:
                left+=1
print(res)
