import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(input().split())
visited=[0 for _ in range(10)]
v=[]
def chk(op,a,b):
    if op=='<':
        return a<b
    else:
        return a>b
def go(cnt,s,back):
    if cnt==N:
        v.append(int(s))
        return
    for i in range(10):
        if not visited[i] and chk(a[cnt],back,i):
            visited[i]=1
            go(cnt+1,s+str(i),i)
            visited[i]=0
for i in range(10):
    visited[i]=1
    go(0,str(i),i)
    visited[i]=0
v.sort()
res1=str(v[len(v)-1])
res2=str(v[0])
if len(res1)<=N:
    res1='0'+res1
if len(res2)<=N:
    res2='0'+res2
print(res1)
print(res2)