import sys
def input():return sys.stdin.readline().rstrip()
N,M,P=map(int,input().split())
res=1
if N:
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)

    cnt=0
    for cur in arr:
        if cur>=M:
            if cur==M:
                cnt+=1
                continue
            res+=1
    if res+cnt>P:
        res=-1
print(res)