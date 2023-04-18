import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
left=0
right=N-1
r=int(1e10)
res1=-1
res2=-1
while left<right:
    s=a[left]+a[right]
    if abs(s) <=abs(r):
        r = abs(s)
        res1 = a[left]
        res2 = a[right]
    if s>=0:
        right-=1
    else:
        left+=1
print(res1,res2)