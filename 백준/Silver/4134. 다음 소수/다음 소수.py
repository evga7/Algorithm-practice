import sys
import math
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
T=int(input())
def chk(num):
    for i in range(2,int(math.sqrt(num))+1):
        if not num%i:
            return False
    return True
while T:
    T-=1
    N=int(input())
    if N<=2:
        print(2)
        continue
    if N>4*int(1e9):continue
    while True:
        if chk(N):
            print(N)
            break
        N+=1