import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(input().split())
a.sort()
def chk(c):
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        return 1
    return 0
def go(idx,cnt,A,B,S):
    if cnt==N:
        if A>0 and B>1:
            print(S)
        return
    for i in range(idx,M):
        if chk(a[i]):
            go(i+1,cnt+1,A+1,B,S+a[i])
        else:
            go(i + 1, cnt + 1, A , B+1, S + a[i])
go(0,0,0,0,"")
        