import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,R,C=map(int,input().split())
res=0
def go(s,r,c):
    global res
    if r==R and c==C:
        print(res)
        exit(0)
    if R<r+s and r<=R and c<=C and C<c+s:
        half=s//2
        go(half,r,c)
        go(half, r, c+half)
        go(half, r + half, c)
        go(half, r+half, c + half)
    else:
        res+=s*s
S=pow(2,N)
go(S,0,0)
print(res)
        