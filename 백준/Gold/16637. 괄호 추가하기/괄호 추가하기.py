import sys
def input():
    return sys.stdin.readline().rstrip()
N=int(input())
s=input()
res=-sys.maxsize
def cal(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
def go(idx,su):
    if idx>=N-1:
        global res
        res=max(res,su)
        return
    if idx+4<N:
        go(idx+4,cal(su,cal(int(s[idx+2]),int(s[idx+4]),s[idx+3]),s[idx+1]))
    go(idx+2,cal(su,int(s[idx+2]),s[idx+1]))
go(0,int(s[0]))
print(res)
