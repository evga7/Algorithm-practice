N,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
mid=0
def go(idx,num):
    if idx==N:
        return 0
    if dp[idx][num]!=-1:
        return dp[idx][num]
    ret=0
    for i in range(idx,N):
        if num-b[i]>=0:
            ret=max(ret,go(i+1,num-b[i])+a[i])
    dp[idx][num]=ret
    return dp[idx][num]
res=0
dp = [[-1 for _ in range(10001)] for _ in range(N + 1)]
for i in range(10001):
    mid=i
    if go(0,i)>=M:
        print(i)
        exit(0)
        