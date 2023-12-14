import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=list(map(int,input().split()))
st=set()
def go(idx,s):
    if idx>=N:
        st.add(s)
        return
    go(idx+1,s+a[idx])
    go(idx+1,s)
go(0,0)
for i in range(1,2000001):
    if i in st:continue
    print(i)
    exit(0)