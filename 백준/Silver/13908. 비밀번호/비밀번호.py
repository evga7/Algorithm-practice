import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N,M=map(int,input().split())
a=list(input().split())
st = set(a)
res=0
def chk(s):
    for cur in st:
        if not cur in s:
            return False
    return True
def go(cnt,s):
    if cnt==N:
        if chk(s):
            global res
            res+=1
        return
    for i in range(10):
        go(cnt+1,s+str(i))
go(0,"")
print(res)