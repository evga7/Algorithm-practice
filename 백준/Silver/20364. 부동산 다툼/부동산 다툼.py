import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
st=set()
def go(cur):
    x=cur
    res=0
    while x:
        if x in st:
            res=x
        x//=2
    if not res:
        st.add(cur)
    print(res)
for i in range(M):
    cur=int(input())
    go(cur)