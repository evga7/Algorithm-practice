import bisect
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
T=int(input())
while T:
    T-=1
    N,M=map(int,input().split())
    a=list(map(int,input().split()))
    b = list(map(int, input().split()))
    b.sort()
    res=0
    for cur in a:
        res+=bisect.bisect(b,cur-1)
    print(res)