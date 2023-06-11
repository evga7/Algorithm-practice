import bisect
import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[]
for i,cur in enumerate(a):
    res.append(bisect.bisect_right(b,cur)-i-1)
print(*res)