import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N,M=map(int,input().split())
t=[0 for _ in range(N+1)]
for i in range(M):
    a=list(map(int,input().split()))
    w=a[1]
    if len(a)>2:
        e=a[2]-1
    if a[0]==1:
        t[w]|=(1<<e)
    elif a[0]==2:
        t[w]&= ~ (1<<e)
    elif a[0]==4:
        t[w]>>=1
    else:
        t[w]<<=1
        t[w]&=((1<<20)-1)
st=set()
for i in range(1,N+1):
    st.add(t[i])
print(len(st))