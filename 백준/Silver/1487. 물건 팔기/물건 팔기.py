import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
a.sort()
b=[]
res_s=0
res=0
for x,y in a:
    b.append(x)
for cur in b:
    s=0
    for x,y in a:
        if cur<=x:
            if cur-y>0:
                s+=cur-y
    if res_s<s:
        res_s=s
        res=cur
print(res)