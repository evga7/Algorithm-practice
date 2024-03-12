import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[list(input()) for _ in range(N)]
res=987654321
for bit in range(1<<N):
    temp=[a[i][:] for i in range(N)]
    for i in range(N):
        if bit & (1<<i):
            for j in range(N):
                if temp[i][j]=='H':
                    temp[i][j]='T'
                else:
                    temp[i][j]='H'
    c=0
    for i in range(N):
        cnt=0
        for j in range(N):
            if temp[j][i]=='T':
                cnt+=1
        c+=min(cnt,N-cnt)
    res=min(res,c)
print(res)
