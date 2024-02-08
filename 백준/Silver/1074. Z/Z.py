import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,R,C=map(int,input().split())
res=0
def go(x,y,s):
    global res
    if x==R and y==C:
        print(res)
        exit(0)
    if R<x+s and x<=R and y<=C and y+s>C:
        half=s//2
        go(x,y,half)
        go(x,y+half,half)
        go(x+half, y,half)
        go(x+half,y+half,half)
    else:
        res+=s*s
    
go(0,0,1<<N)