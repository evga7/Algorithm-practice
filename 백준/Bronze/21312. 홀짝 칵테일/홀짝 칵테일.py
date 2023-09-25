import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
st=set()
def go(cnt,idx,num):
    if cnt>=4:
        return
    if cnt and num:
        st.add(num)
    for i in range(idx,3):
        go(cnt+1,i+1,num*a[i])
        
a=list(map(int,input().split()))
go(0,0,1)
ar=list(st)
res=-1
for cur in ar:
    if cur&1:
        res=max(res,cur)
if res==-1:
    ar.sort(reverse=True)
    res=ar[0]

print(res)