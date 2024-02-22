import sys
def input():return sys.stdin.readline().rstrip()
v=[]
def go(idx,cnt):
    if cnt==6:
        print(*v)
        return
    for i in range(idx,N):
        v.append(a[i])
        go(i+1,cnt+1)
        v.pop()
        
while True:
    N,*a=map(int,input().split())
    if not N:
        break
    go(0,0)
    print('')