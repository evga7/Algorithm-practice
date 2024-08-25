import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
v=[]
cnt=1
v.append(666)
idx=1666
while cnt<=N:
    if str(idx).count("666"):
        v.append(idx)
        cnt+=1
    idx+=1
print(v[N-1])