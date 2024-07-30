import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
s=input()
st=[]
f=0
temp = ""
for cur in s:
    if cur=='<':
        f=1
        if temp:
            print(temp[::-1],end='')
            temp=""
        temp+=cur
    elif cur==">":
        f=0
        print(temp+'>',end='')
        temp=""
    elif cur==' ':
        if not f:
            print(temp[::-1],end=' ')
            temp=""
        else:
            temp+=cur
    else:
        temp+=cur
if temp and not f:
    print(temp[::-1],end=' ')
    temp=""
else:
    temp+=' '