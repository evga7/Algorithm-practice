import sys
def input(): return sys.stdin.readline().rstrip()
T=int(input())
def go(bit,idx,s):
    if idx==11:
        global res
        if bit==2047:
            res=max(res,s)
        return
    for i in range(11):
        if a[idx][i] and not bit & (1<<i):
            go(bit|(1<<i),idx+1,s+a[idx][i])
while T:
    T-=1
    a=[list(map(int,input().split())) for _ in range(11)]
    res=0
    go(0,0,0)
    print(res)