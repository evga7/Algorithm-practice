import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
a.sort()
pos=0
res=0
cnt=0
for cur in a:
    res+=cnt+cur
    cnt+=cur
    pos=cur
print(res)