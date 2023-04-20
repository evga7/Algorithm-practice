import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[0 for _ in range(N+1)]
for i in range(1,N+1):
    num=int(input())
    a[i]=num
visited=[0 for _ in range(N+1)]
v=[]
st=set()
def go(start,cur,cnt):
    if start==cur and cnt>0:
        for cur in v:
            st.add(cur)
        return
    if visited[cur]:
        return
    visited[cur]=1
    v.append(cur)
    go(start,a[cur],cnt+1)
    v.pop()
for i in range(1,N+1):
    if a[i]==i:
        st.add(i)
        continue
    visited = [0 for _ in range(N + 1)]
    go(i,i,0)
res=list(st)
res.sort()
print(len(res))
for cur in res:
    print(cur)