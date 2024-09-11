import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
M=int(input())
a=list(map(int,input().split()))
a.sort()
b=[]
for i in range(1,N):
    b.append(a[i]-a[i-1])
b.sort()
res=0
for i in range(N-M):
    res+=b[i]
print(res)