import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
st=[]
def go(idx,cnt,num):
    if cnt>11 or num in st:
        return
    st.append(num)
    for i in range(idx,-1,-1):
        go(i-1,cnt+1,(num*10)+i)
go(9,0,0)
a=sorted(list(st))
if len(st)<N:
    print(-1)
else:
    print(a[N-1])