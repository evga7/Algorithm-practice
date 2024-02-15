import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
st=[]
for i in range(N):
    s=list(input().split())
    if s[0]=='push':
        st.append(s[1])
    elif s[0]=='pop':
        if st:
            print(st.pop())
        else:
            print(-1)
    elif s[0]=='size':
        print(len(st))
        
    elif s[0]=='empty':
        if st:
            print(0)
        else:
            print(1)
    elif s[0]=='top':
        if st:
            print(st[-1])
        else:
            print(-1)