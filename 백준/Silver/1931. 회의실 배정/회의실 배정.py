import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
a.sort(key=lambda x :(x[1],x[0]))
pos=0
res=0
for cur in a:
    x,y=cur[0],cur[1]
    if x>=pos:
        pos=y
        res+=1
print(res)