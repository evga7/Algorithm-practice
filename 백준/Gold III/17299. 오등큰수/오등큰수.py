from collections import *
# sys.setrecursionlimit(100000)
import sys
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
c=Counter(a)
st=[]
b=[-1 for _ in range(N)]
for i in range(N):
    cur=a[i]
    while st and c[a[st[-1]]]<c[cur]:
        b[st[-1]]=a[i]
        st.pop()
    st.append(i)
print(*b)