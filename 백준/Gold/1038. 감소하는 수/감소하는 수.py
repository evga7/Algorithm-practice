import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
v=[]
def go(idx,cnt,num):
    if cnt==11 or (not num and cnt>1):
        return 
    if num:
        v.append(num)
    for i in range(idx,-1,-1):
        go(i-1,cnt+1,(num*10)+i)
go(9,0,0)
v.append(0)
v.sort()
if len(v)>N:
    print(v[N])
else:
    print(-1)