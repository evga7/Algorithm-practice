dp=[[-1 for _ in range(501)] for _ in range(501)]
def go(x,y,t):
    if y>=x+1 or x==len(t):
        return 0
    if dp[x][y]!=-1:
        return dp[x][y]
    ret=0
    ret+=max(ret,go(x+1,y+1,t),go(x+1,y,t))+t[x][y]
    dp[x][y]=ret
    return dp[x][y]
def solution(triangle):
    return go(0,0,triangle)