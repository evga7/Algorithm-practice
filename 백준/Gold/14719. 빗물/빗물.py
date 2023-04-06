import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
arr=list(map(int,input().split()))
res=0
for i,cur in enumerate(arr):
    lm=cur
    rm=cur
    if i>0:
        lm=max(lm,max(arr[:i]))
    if i<len(arr)-1:
        rm=max(rm,max(arr[i:]))
    res+=min(rm,lm)-cur
print(res)