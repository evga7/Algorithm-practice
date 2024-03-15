import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[]
for i in range(N):
    q,w,e,r=input().split()
    w,e,r=int(w),int(e),int(r)
    a.append((q,w,e,r))
a.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for cur in a:
    print(cur[0])