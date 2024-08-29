import itertools
import math
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N,M=map(int,input().split())
s=M-N
if s<=3:
    print(s)
    exit(0)
n=int(math.sqrt(s))
e=s-n**2
res=n*2-1
if math.pow(n,2)==s:
    print(res)
elif e<=n:
    print(res+1)
else:
    print(res+2)

