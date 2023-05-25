import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
st=set()
for i in range(M):
    num=int(input())
    st.add(num)
dp=[[-1 for _ in range(501)] for _ in range(10001)]
def go(idx,speed):
    if idx==N:
        return 0
    if dp[idx][speed]!=-1:
        return dp[idx][speed]
    ret=987654321
    for cur in (speed+1,speed,speed-1):
        if cur>0 and idx+cur<=N and not idx+cur in st:
            ret=min(ret,go(idx+cur,cur)+1)
    dp[idx][speed]=ret
    return dp[idx][speed]
res=go(1,0)
if res==987654321:
    res=-1
print(res)