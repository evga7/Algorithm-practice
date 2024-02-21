import sys
def input():return sys.stdin.readline().rstrip()
E,S,M=map(int,input().split())
e,s,m=1,1,1
def go(e,s,m):
    if m==20:
        m=1
    if s==29:
        s=1
    if e==16:
        e=1
    return (e,s,m)
cnt=1
while e!=E or s!=S or m!=M:
    e+=1
    s+=1
    m+=1
    cnt+=1
    e,s,m=go(e,s,m)
print(cnt)