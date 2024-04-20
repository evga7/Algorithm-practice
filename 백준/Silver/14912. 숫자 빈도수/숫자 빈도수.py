import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
N,M=map(int,input().split())
res=0
M=str(M)
for i in range(1,N+1):
    res+=str(i).count(M)
print(res)