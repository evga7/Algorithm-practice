import sys
sys.setrecursionlimit(130000)
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
ar=[]
d=[[-1 for _ in range(10001)]for _ in range(13)]
for i in range(N):
    a,b,c=map(int,input().split())
    if b>M or b-a<c:continue
    ar.append((a,b,c))
ar.sort()
def go(idx,pos):
    if pos==M:
        return 0
    if d[idx][pos]!=-1:
        return d[idx][pos]
    ret=987654321
    ret=min(go(idx,pos+1)+1,ret)
    for i in range(idx,len(ar)):
        cur=ar[i]
        st=cur[0]
        end=cur[1]
        cost=cur[2]
        if st==pos:
            ret=min(ret,go(i+1,end)+cost)
    d[idx][pos]=ret
    return d[idx][pos]
print(go(0,0))