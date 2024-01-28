import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
# map(int,input().split())
INF = sys.maxsize
N=int(input())
left=1
right=1
s=1
res=0
while right<=N:
    if s>=N:
        if s==N:
            res+=1
        s-=left
        left+=1
    else:
        right+=1
        s+=right
print(res)