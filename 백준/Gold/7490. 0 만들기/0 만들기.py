import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
T=int(input())
def go(idx,num,s):
    if idx>=N+1:
        if num==0:
            res.append(s)
        return
    go(idx+1,num+idx,s+"+"+str(idx))
    go(idx + 1, num - idx, s + "-" + str(idx))
    if idx+1<=N:
        go(idx + 2, num + ((idx*10)+(idx+1)), s +"+"+ str(idx)+" "+str(idx+1))
        go(idx + 2, num - ((idx * 10) + (idx + 1)), s + "-" + str(idx) + " " + str(idx + 1))
    
    
while T:
    res=[]
    T-=1
    N=int(input())
    go(3,12,"1 2")
    go(2,1,"1")
    res.sort()
    for cur in res:
        print(cur)
    print('')