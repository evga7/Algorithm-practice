import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
st=set()
def go(num,idx):
    if num in st:
        return
    st.add(num)
    for i in range(idx,-1,-1):
        go(num*10+i,i-1)
for i in range(9,-1,-1):
    go(i,i-1)
a=list(st)
a.sort()
if N>=len(a):
    print(-1)
else:
    print(a[N])