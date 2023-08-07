import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
X,Y,P1,P2=map(int,input().split())
x=set(range(P1,10**6,X))
y=set(range(P2,10**6,Y))
res=x&y
print(min(res) if res else -1)

