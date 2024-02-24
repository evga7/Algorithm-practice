import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input())) for _ in range(N)]
res=0
def go(bit):
    s=0
    for i in range(N):
        ss=0
        for j in range(M):
            idx=i*M+j
            if bit & (1<<idx):
                ss=ss*10+a[i][j]
            else:
                s += ss
                ss = 0
        s += ss
    for i in range(M):
        ss=0
        for j in range(N):
            idx=j*M+i
            if bit & (1<<idx):
                s+=ss
                ss=0
            else:
                ss=ss*10+a[j][i]
        s+=ss
    return s
    
for i in range(1<<(N*M)):
    res=max(res,go(i))
print(res)