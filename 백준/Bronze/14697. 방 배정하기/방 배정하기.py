*a,d=list(map(int,input().split()))
dp=[-1 for _ in range(d+1)]
def go(idx):
    if idx==0:
        return 1
    if dp[idx]!=-1:
        return dp[idx]
    ret=0
    for cur in a:
        c=idx//cur
        for i in range(1,c+1):
            ret=max(ret,go(idx-(cur*i)))
    dp[idx]=ret
    return dp[idx]
print(go(d))