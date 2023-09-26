import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
def chk(c1,c2):
    if c1=='i':
        if c2=='j' or c2=='l':
            return True
    if c1=='v':
        if c2=='w':
            return True
    if c1==c2:
        return True
    return False
s=input()
s2=input()
def go():
    dp=[[0 for _ in range(len(s2)+1)] for _ in range(len(s)+1)]
    for i in range(1,len(s)+1):
        dp[i][0]=i
    for i in range(1,len(s2)+1):
        dp[0][i]=i
    for i in range(1,len(s)+1):
        for j in range(1,len(s2)+1):
            if chk(s[i-1],s2[j-1]):
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
    return dp[len(s)][len(s2)]
print(go())
    