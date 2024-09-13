import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]
def uni(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if x < y:
            p[y] = x
        else:
            p[x] = y
        return True
    return False
idx = 0
while True:
    idx += 1
    N, M = map(int, input().split())
    if not N and not M:
        break
    p = [i for i in range(N+1)]
    f = 1
    st2=set()
    for i in range(M):
        x,y=map(int,input().split())
        if not uni(x,y):
            st2.add(find(x))
    print("Case %d:" % idx, end=' ')
    st = set()
    f = 1
    st3=set()
    for cur in st2:
        st3.add(find(cur))
    for i in range(1, N + 1):
        c=find(i)
        if not c in st3:
            st.add(c)
    res = len(st)
    if not res:
        print("No trees.")
        continue
    if res > 1:
        print("A forest of %d trees." % res)
    elif res == 1:
        print("There is one tree.")