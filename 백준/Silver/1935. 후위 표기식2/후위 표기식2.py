from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
s=input()
a=deque(input() for _ in range(N))
op=[]
num=[]
m=defaultdict(str)
for i,cur in enumerate(a):
    m[chr(65+i)]=cur
for cur in s:
    if cur.isalpha():
        num.append(m[cur])
    else:
        c,d=num.pop(),num.pop()
        num.append(str(eval(d+cur+c)))
print('%.2f'%float(num[0]))