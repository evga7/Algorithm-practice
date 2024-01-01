import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=[list(input()) for _ in range(N)]
for i in range(len(a[0])):
    st=set()
    for j in range(N):
        st.add(a[j][i])
        if len(st)>1:
            print('?',end='')
            break
    if len(st)==1:
        print(st.pop(),end='')
            
    