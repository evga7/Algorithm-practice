import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
res=0
idx=0
for cur in a:
    if idx>=cur:continue
    idx=cur+M-1
    res+=1
print(res)