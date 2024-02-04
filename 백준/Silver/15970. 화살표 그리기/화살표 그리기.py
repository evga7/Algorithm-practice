import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
w=[]
b=[]
res=0
for i in range(N):
    z,x=map(int,input().split())
    if x==1:
        w.append(z)
    else:
        b.append(z)
w.sort()
b.sort()
for i in range(1,len(w)-1):
    res+=min(w[i]-w[i-1],w[i+1]-w[i])
for i in range(1, len(b)-1):
    res+=min(b[i]-b[i-1],b[i+1]-b[i])
if len(w)>1:
    res+=w[1]-w[0]
    res += w[len(w) - 1] - w[len(w) - 2]
if len(b)>1:
    res+=b[1]-b[0]
    res+=b[len(b)-1]-b[len(b)-2]
print(res)
