import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N,M=map(int,input().split())
a=list(map(int,input().split()))
for i in range(M):
    q,w,e=map(int,input().split())
    w-=1
    if q==1:
        a[w]=e
    elif q==2:
        for i in range(w,e):
            a[i]=1-a[i]
    elif q==3:
        for i in range(w, e ):
            a[i] = 0
    elif q==4:
        for i in range(w, e):
            a[i] = 1
print(*a)