import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N,M=map(int,input().split())
res=0
if N:
    a=list(map(int,input().split()))
    s=0
    for cur in a:
        if s+cur>M:
            s=0
            res+=1
        s+=cur
    if s:
        res+=1
print(res)