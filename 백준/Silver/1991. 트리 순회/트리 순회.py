import sys
#sys.setrecursionlimit(10000)
def input():return sys.stdin.readline().rstrip()
N=int(input())
t={}
for i in range(N):
    a,b,c=list(input().split())
    t[a]=[b,c]
def pre(cur):
    if cur=='.':
        return
    print(cur,end='')
    pre(t[cur][0])
    pre(t[cur][1])
def ino(cur):
    if cur=='.':
        return
    ino(t[cur][0])
    print(cur,end='')
    ino(t[cur][1])
def post(cur):
    if cur=='.':
        return
    post(t[cur][0])
    post(t[cur][1])
    print(cur,end='')
pre('A')
print('')
ino('A')
print('')
post('A')