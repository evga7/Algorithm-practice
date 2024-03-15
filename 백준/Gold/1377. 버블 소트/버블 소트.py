import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[]
for i in range(N):
    num=int(input())
    a.append((num,i))
b=sorted(a)
res=0
for i in range(N):
    res=max(res,b[i][1]-a[i][1])
print(res+1)
    