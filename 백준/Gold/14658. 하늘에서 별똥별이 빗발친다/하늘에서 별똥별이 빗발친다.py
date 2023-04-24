import sys
def input():return sys.stdin.readline().rstrip()
N,M,L,K=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(K)]
def go(x,y):
    cnt=0
    for cur in a:
        xx,yy=cur[0],cur[1]
        if x<=xx<=x+L and y<=yy<=y+L:
            cnt+=1
    return cnt
res=0
for cur in a:
    for cur2 in a:
        res=max(res,go(cur[0],cur2[1]))
print(K-res)