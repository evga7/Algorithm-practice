import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
for i in range(N):
    s=input()
    st=[]
    f=0
    for cur in s:
        if cur==')':
            if not st:
                f=1
                break
            st.pop()
            continue
        st.append(cur)
    if not f and not st:
        print("YES")
    else:
        print("NO")