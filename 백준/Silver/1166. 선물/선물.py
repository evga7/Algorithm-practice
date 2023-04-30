import sys
def input():return sys.stdin.readline().rstrip()
N,L,W,H=map(int,input().split())
left=0
right=max(L,W,H)
for i in range(10000):
    mid=(left+right)/2
    if (L//mid)*(W//mid)*(H//mid)<N:
        right=mid
    else:
        left=mid
print("%.10f"%left)