d=[0 for _ in range(100001)]
def solution(n, money):
    answer = 0
    d[0]=1
    for cur in money:
        for i in range(cur,n+1):
            d[i]+=d[i-cur]%(int(1e9)+7)
    return d[n]