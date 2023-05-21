import sys
def input():return sys.stdin.readline().rstrip()
C,N=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[[[-1 for _ in range(1001)] for _ in range(20)] for _ in range(1001)]
def go(people,idx,cnt):
    if people >= C:
        return 0
    if idx==N:
        if people>=C:
            return 0
        return 987654321
    if dp[people][idx][cnt]!=-1:
        return dp[people][idx][cnt]
    ret=987654321
    cur_cost=a[idx][0]
    cur_p=a[idx][1]
    c=C//cur_p
    for i in range(0,1001):
        ret=min(ret,go(people+i*cur_p,idx+1,c)+i*cur_cost)
    dp[people][idx][cnt]=ret
    return dp[people][idx][cnt]
print(go(0,0,0))