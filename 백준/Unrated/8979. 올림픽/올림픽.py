import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
res=1
a=[list(map(int,input().split())) for _ in range(N)]
a.sort(key=lambda x:(-x[1],-x[2],-x[3]))
g=a[0][1]
s=a[0][2]
d=a[0][3]
for i,cur in enumerate(a):
    if cur[0]==M:
        break
    if g==cur[1] and s==cur[2] and d==cur[3]:continue
    g,s,d=cur[1],cur[2],cur[3]
    res+=1

print(res)