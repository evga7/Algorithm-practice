import sys
import math
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
p=[0 for _ in range(1000001)]
def c():
    for i in range(2,int(math.sqrt(1000001))+1):
        if p[i]:continue
        for j in range(i+i,1000001,i):
            p[j]=1
c()
p[1]=1
st=set()
for i in range(2,1000001):
    if not p[i]:
        st.add(i)
T=int(input())
while T:
    T-=1
    num=int(input())
    res=0
    for i in range(2,num//2+1):
        if num-i in st and i in st :
            res+=1
    print(res)