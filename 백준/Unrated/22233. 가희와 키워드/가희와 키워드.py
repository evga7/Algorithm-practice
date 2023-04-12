import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
st=set()
for i in range(N):
    a=input()
    st.add(a)
for i in range(M):
    a=list(input().split(','))
    for cur in a:
        if cur in st:
            st.remove(cur)
    print(len(st))