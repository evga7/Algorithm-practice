import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
res=0
a.sort()
s=0
for i in range(N):
    if s+1<a[i]:
        break
    s+=a[i]
print(s+1)