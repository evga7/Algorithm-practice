def solution(n):
    answer = 0
    d=[0 for _ in range(100001)]
    d[1]=1
    d[2]=1
    for i in range(3,n+1):
        d[i]=(d[i-1]+d[i-2])%1234567
    return d[n]