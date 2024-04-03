N,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
def go(idx,num):
    if idx==N:
        return 0
    if dp[idx][num]!=-1:
        return dp[idx][num]
    ret=0
    if num-b[idx]>=0:
        ret=max(ret,go(idx+1,num-b[idx])+a[idx])
    ret=max(ret,go(idx+1,num))
    dp[idx][num]=ret
    return dp[idx][num]
res=0
dp = [[-1 for _ in range(10001)] for _ in range(N + 1)]
for i in range(10001):
    if go(0,i)>=M:
        print(i)
        exit(0)