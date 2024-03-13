import sys
import bisect
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
q=[]
q.append(-1)
for cur in a:
    if cur>q[-1]:
        q.append(cur)
    else:
        idx=bisect.bisect_left(q,cur)
        q[idx]=cur
print(len(q)-1)