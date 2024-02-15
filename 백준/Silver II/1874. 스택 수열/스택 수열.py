import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
a=[int(input()) for _ in range(N)]
idx=0
st=[0]
i=0
res=[]
while idx <N and st:
    while a[idx]!=st[-1]:
        i+=1
        if i>N:
            print("NO")
            exit(0)
        st.append(i)
        res.append('+')
    else:
        res.append('-')
        st.pop()
        idx+=1
for cur in res:
    print(cur)