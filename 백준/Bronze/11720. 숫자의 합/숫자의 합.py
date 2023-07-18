import sys
def input(): return sys.stdin.readline().rstrip()
T=int(input())
N=int(input())
res=0
while N:
    res+=N%10
    N//=10
print(res)