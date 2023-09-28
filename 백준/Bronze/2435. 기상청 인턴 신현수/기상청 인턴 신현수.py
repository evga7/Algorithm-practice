import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
a=list(map(int,input().split()))
left=0
s=sum(a[:M])
right=M-1
res=-987654321
while True:
    res=max(res,s)
    right+=1
    if right>=N:
        break
    s+=a[right]
    s-=a[left]
    left+=1
print(res)