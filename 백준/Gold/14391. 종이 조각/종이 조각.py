import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input())) for _ in range(N)]
res=0
def go():
    for cur in range(1<<(N*M)):
        s=0
        ss=0
        for i in range(N):
            s+=ss
            ss=0
            for j in range(M):
                idx=i*M+j
                if cur& 1<<idx:
                    ss=ss*10+a[i][j]
                else:
                    s+=ss
                    ss=0
        if ss:
            s+=ss
            ss=0
        for i in range(M):
            s+=ss
            ss=0
            for j in range(N):
                idx=j*M+i
                if not (cur& 1<<idx):
                    ss=ss*10+a[j][i]
                else:
                    s+=ss
                    ss=0
        if ss:
            s+=ss
        global res
        res=max(res,s)
go()
print(res)