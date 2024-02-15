import sys
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
st=[]
b=[-1 for _ in range(N)]
for i in range(N):
    cur=a[i]
    while st and a[st[-1]]<cur:
        b[st[-1]]=cur
        st.pop()
    st.append(i)
print(*b)