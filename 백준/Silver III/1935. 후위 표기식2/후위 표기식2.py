from collections import *
# sys.setrecursionlimit(100000)
import sys
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
N=int(input())
s=input()
m=defaultdict(int)
ss=0
for i in range(N):
    num=int(input())
    m[chr(65+i)]=num
st=[]
def cal(a,b,op):
    if op=='+':
        return a+b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
    else:
        return a-b
for cur in s:
    cur2=m[cur]
    if cur.isalpha():
        st.append(cur2)
    else:
        a,b=st.pop(),st.pop()
        st.append(cal(float(b),float(a),cur))
print('%.2f'%st[-1])