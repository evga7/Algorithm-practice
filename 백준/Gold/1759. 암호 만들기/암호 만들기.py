import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
b=['' for _ in range(M)]
a=list(input().split())
a.sort()
def chk(s):
    if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
        return True
    return False
def go(idx,cnt):
    if cnt==N:
        aa,bb=0,0
        for i in range(N):
            cur=b[i]
            if chk(cur):
                aa+=1
            else:
                bb+=1
        if aa>=1 and bb>=2:
            print(''.join(b))
        return
    for i in range(idx,M):
        b[cnt]=a[i]
        go(i+1,cnt+1)
        b[cnt]=''
go(0,0)