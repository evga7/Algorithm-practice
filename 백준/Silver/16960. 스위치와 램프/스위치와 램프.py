import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,M=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(N):
    a=list(map(int,input().split()))
    for j in range(1,len(a)):
        g[i+1].append(a[j])
for i in range(1,N+1):
    st=set()
    for j in range(1,N+1):
        if i==j:continue
        for cur in g[j]:
            st.add(cur)
    if len(st)==M:
        print(1)
        exit(0)
print(0)