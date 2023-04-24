import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[input() for _ in range(N)]
b=[]
for i,cur in enumerate(a):
    b.append((cur,i))
m=0
b.sort()
l=[0 for _ in range(N+1)]
for i in range(N-1):
    c,d=b[i][0],b[i+1][0]
    e,f=b[i][1],b[i+1][1]
    cnt=0
    for j in range(min(len(c),len(d))):
        if c[j]!=d[j]:break
        cnt+=1
    l[e]=max(l[e],cnt)
    l[f] = cnt
    if m<cnt:
        m=cnt
b.sort(key=lambda x:x[0])
cnt=0
f=0
r=''
for i,cur in enumerate(a):
    if not f:
        if l[i]==m:
            f=1
            print(cur)
            r=cur[:m]
    else:
        if l[i]==m and cur[:m]==r:
            print(cur)
            break
