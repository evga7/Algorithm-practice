from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
A,B,C=map(int,input().split())
q=deque()
st=set()
q.append((A,B,C))
def c(x,y):
    if x<y:
        return (x,y)
    return (y,x)
while q:
    x,y,z=q.popleft()
    if x==y and y==z:
        print(1)
        exit(0)
    if x!=y:
        xx,yy=c(x,y)
        if not (xx,yy) in st:
            st.add((xx,yy))
            q.append(((xx+xx,yy-xx,z)))
    if x!=z:
        xx,zz=c(x,z)
        if not (xx,zz) in st:
            st.add((xx,zz))
            q.append(((xx+xx,y,zz-xx)))
    if y!=z:
        yy,zz=c(y,z)
        if not (yy,zz) in st:
            st.add((yy,zz))
            q.append(((x,yy+yy,zz-yy)))
    
print(0)