import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[int(input()) for _ in range(N)]
c=[]
d=[]
for cur in a:
    if cur<=0:
        c.append(cur)
    else:
        d.append(cur)
c.sort()
d.sort(reverse=True)
q=[]
res=0
back=-1001
for cur in c:
    if cur<=0:
        if back!=-1001:
            res+=max(back*cur,back+cur)
            back=-1001
            continue
    else:
        if back!=-1001:
            if back<=0:
                res+=back
            else:
                res+=max(back*cur,back+cur)
                back=-1001
                continue
    back=cur
if back!=-1001:
    res+=back
back=-1001
for cur in d:
    if cur<=0:
        if back!=-1001:
            res+=max(back*cur,back+cur)
            back=-1001
            continue
    else:
        if back!=-1001:
            if back<=0:
                res+=back
            else:
                res+=max(back*cur,back+cur)
                back=-1001
                continue
    back=cur
if back!=-1001:
    res+=back
if N==1:
    print(a[0])
else:
    print(res)
    