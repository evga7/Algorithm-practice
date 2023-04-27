import sys
def input():return sys.stdin.readline().rstrip()
T=int(input())

op=[6,2,5,5,4,5,6,3,7,6]
def go(idx,cnt,s):
    if idx==0:
        return s
    if dp[idx][cnt]!=-1:
        return dp[idx][cnt]
    ret=int('9'*51)
    if s and idx-op[0]>=0:
        ret=min(ret,go(idx-op[0],cnt+1,s*10))
    for i in range(1,10):
        if idx-op[i]>=0:
            ret=min(ret,go(idx-op[i],cnt+1,s*10+i))
    dp[idx][cnt]=ret
    return dp[idx][cnt]

while T:
    T-=1
    N=int(input())
    N2=N
    res2=''
    if N2&1:
        N2-=3
        res2+='7'
    res2+='1'*(N2//2)
    dp = [[-1 for _ in range(101)] for _ in range(101)]
    print(go(N,0,0),end=' ')
    print(res2)