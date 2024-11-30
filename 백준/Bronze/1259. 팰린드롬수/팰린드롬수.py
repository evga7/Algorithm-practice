import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
def chk(left,right):
    while left<right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            break
    return left>=right
while True:
    s=input()
    if s=="0":
        break
    if chk(0,len(s)-1):
        print("yes")
    else:
        print("no")