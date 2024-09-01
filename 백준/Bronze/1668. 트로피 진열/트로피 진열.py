import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=[int(input()) for _ in range(N)]
res1,res2=1,1
s=0
cnt=0
for cur in a:
    if s<cur:
        cnt+=1
        res1=max(res2,cnt)
    s=max(s,cur)
a=a[::-1]
cnt=1
s=a[0]
for cur in a:
    if s<cur:
        cnt+=1
        res2=max(res2,cnt)
    s=max(s,cur)
print(res1)
print(res2)