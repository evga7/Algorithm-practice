import sys
def input():return sys.stdin.readline().rstrip()
dp=[[[-1 for _ in range(100)] for _ in range(100)] for _ in range(20)]
s=input()
D=input()
A=input()
def go(idx,x,y):
    if idx==len(s):
        return 1
    if dp[idx][x][y]!=-1:
        return dp[idx][x][y]
    ret=0
    n_x=1-x
    for i in range(y,len(D)):
        if n_x == 1:
            if A[i]==s[idx]:
                ret+=go(idx+1,n_x,i+1)
        else:
            if D[i]==s[idx]:
                ret+=go(idx+1,n_x,i+1)
    dp[idx][x][y]=ret
    return dp[idx][x][y]
res=0
for i in range(len(D)):
    if D[i]==s[0]:
        res+=go(1,0,i+1)
    if A[i]==s[0]:
        res+=go(1,1,i+1)
print(res)