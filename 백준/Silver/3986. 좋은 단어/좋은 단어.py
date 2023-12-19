import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
res=0
for i in range(N):
    s=input()
    st=[]
    for cur in s:
        if st and st[-1]==cur:
            st.pop()
            continue
        st.append(cur)
    if not st:
        res+=1
print(res)