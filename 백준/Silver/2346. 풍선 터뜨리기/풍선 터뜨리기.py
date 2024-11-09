import sys

def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N=int(input())
a=list(map(int,input().split()))
b=[]
idx=0
for i,cur in enumerate(a):
    if cur<0:
        b.append((i + 1, cur))
    else:
        b.append((i+1,cur-1))

idx=0
l=N
while b:
    print(b[idx][0],end=' ')
    cur=idx
    l-=1
    n=b[idx][1]
    del b[idx]
    if not b:
        break
    pos=(idx+n)%l
    idx=pos