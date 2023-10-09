import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
S=list(str(N+1))
def go(s,pos):
    if s.count('5')>=M:
        print(''.join(s))
        exit(0)
    while s[pos]=='5' and pos-1>=0:
        pos-=1
    num=int(''.join(s))
    num=num+pow(10,len(s)-pos-1)
    go(list(str(num)),len(s)-1)
go(S,len(S)-1)        
        