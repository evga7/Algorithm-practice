import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
M=N//2
res=987654321
def go2(bit):
    s1=0
    s2=0
    for i in range(N):
        for j in range(i+1,N):
            if i==j:continue
            s=a[i][j]+a[j][i]
            if bit & (1<<i) and bit & (1<<j):
                s1+=s
            elif not bit & (1<<i) and not bit & (1<<j) :
                s2+=s
    return abs(s1-s2)
def go(bit):
    global res
    res=min(res,go2(bit))

for i in range(1,1<<N):
    go(i)
print(res)
        