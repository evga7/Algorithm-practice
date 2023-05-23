import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
st=set()
for i in range(1,100001):
    st.add(i*i)
f=0
for i in range(1,100001):
    if i*i-N in st:
        print(i)
        f=1
if not f:
    print(-1)