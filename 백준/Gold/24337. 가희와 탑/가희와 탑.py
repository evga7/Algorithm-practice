import sys
def input():return sys.stdin.readline().rstrip()
N,A,B=map(int,input().split())
r=[]
for i in range(A-1):
    r.append(i+1)
r.append(max(A,B))
for i in range(B-1,0,-1):
    r.append(i)
if len(r)>N:
    print(-1)
    exit(0)
elif len(r)<N:
    print(r[0],end=' ')
    for i in range(N-len(r)):
        print(1,end=' ')
    print(*r[1:])
else:
    print(*r)