import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
arr=[]
for i in range(N):
    a,b=input().split()
    a=int(a)
    arr.append((a,b,i))
arr.sort(key=lambda x:(x[0],x[2]))
for cur in arr:
    print(cur[0],cur[1])