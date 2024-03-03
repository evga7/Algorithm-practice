import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
s=list(map(int,input()))
s2=list(map(int,input()))
def go(start,cnt,op):
    temp=s[:]
    if op:
        temp[0]=1-temp[0]
        temp[1]=1-temp[1]
    for i in range(start,N):
        if temp[i-1]!=s2[i-1]:
            cnt+=1
            for j in range(i-1,min(N,i+2)):
                temp[j]=1-temp[j]
    if temp==s2:
        return cnt
    return 987654321
res=987654321
res=min(res,go(1,0,0),go(1,1,1))
if res==987654321:
    res=-1
print(res)