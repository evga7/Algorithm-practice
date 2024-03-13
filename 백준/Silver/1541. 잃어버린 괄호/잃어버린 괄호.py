import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
a=input()
q=[]
op=0
temp=""
res=0
for i in range(len(a)+1):
    cur=""
    if i<len(a):
        cur=a[i]
    if cur.isdigit():
        temp+=cur
    else:
        if op:
            res-=int(temp)
        else:
            res+=int(temp)
        if cur=='-':
            op=1
        temp=""
print(res)