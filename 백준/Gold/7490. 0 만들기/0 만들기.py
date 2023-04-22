import sys
def input():return sys.stdin.readline().rstrip()
T=int(input())
v=[]
def go(cnt,s,st):
    if cnt>N:
        if s==0 and cnt==N+1:
            v.append(st)
        return
    go(cnt + 1, s + cnt, st +'+'+ str(cnt))
    go(cnt + 1, s - cnt, st +'-'+ str(cnt))
    go(cnt + 2, s+(cnt*10+(cnt+1)), st +'+'+str(cnt)+' '+str(cnt+1))
    go(cnt+2,s-(cnt*10+(cnt+1)),st+'-'+str(cnt)+' '+str(cnt+1))

while T:
    T-=1
    N=int(input())
    go(2,1,'1')
    go(3,12,'1 2')
    v.sort()
    for cur in v:
        print(cur)
    print('')
    v.clear()