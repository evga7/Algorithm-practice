import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N = int(input())
a=[list(input()) for _ in range(N)]
a.sort(key=lambda x:-len(x))
p=[0 for _ in range(26)]
for i in range(N):
    s=pow(10,len(a[i])-1)
    for j in range(len(a[i])):
        p[ord(a[i][j])-ord('A')]+=s
        s//=10
p.sort(reverse=True)
res=0
num=9
for i in range(26):
    res+=p[i]*num
    num-=1
print(res)