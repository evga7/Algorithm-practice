import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
st=set()
def go(num,idx):
    if num in st:
        return
    st.add(num)
    for i in range(idx,-1,-1):
        go(num*10+i,i-1)
go(0,9)
a=sorted(list(st))
if N>=len(st):
    print(-1)
else:
    print(a[N])
        