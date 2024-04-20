import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
N,M=map(int,input().split())
st=set()
rest=set()
def go(idx,s):
    if idx==N:
        rest.add(s)
        return
    if s in st:
        return
    if s:
        st.add(s)
    for i in range(1,4):
        if idx+i<=N:
            go(idx+i,s+'+'+str(i))
for i in range(1,4):
    go(i,str(i))
v=sorted(list(rest))
if len(v)<M:
    print(-1)
else:
    print(v[M-1])