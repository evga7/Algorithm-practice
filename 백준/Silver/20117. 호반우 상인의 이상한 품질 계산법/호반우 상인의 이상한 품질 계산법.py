import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
a.sort()
left=0
right=N-1
res=0
if N&1:
    res+=a[N//2]
while left<right:
    res+=a[right]*2
    right-=1
    left+=1
print(res)