import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
s=list(input())
l=[[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
res=0
t,g,f,p=0,0,0,0
l[0][0][0][0]=1
for i in range(N):
    cur=s[i]
    if cur=='T':
        t=(t+1)%3
    elif cur=='G':
        g = (g + 1) % 3
    elif cur == 'F':
        f = (f + 1) % 3
    elif cur == 'P':
        p = (p + 1) % 3
    res+=l[t][g][f][p]
    l[t][g][f][p]+=1
print(res)