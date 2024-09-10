import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N,M=map(int,input().split())
st=set(map(int,input().split()))
while True:
    temp=N
    f=1
    while temp:
        if not temp%10 in st:
            break
        temp//=10
    if not temp:
        break
    N-=1
print(N)