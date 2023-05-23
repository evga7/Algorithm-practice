import sys
def input():return sys.stdin.readline().rstrip()
A,B=map(int,input().split())
st=set()
chk=[1 for _ in range(10000001)]
def ch():
    for i in range(2,10000001):
        if not chk[i]:continue
        for j in range(i*i,10000001,i):
            chk[j]=0
ch()
for i in range(2,10000001):
    if chk[i]:
        num=pow(i,2)
        cnt=2
        while num<=pow(10,14):
            st.add(num)
            cnt+=1
            num=pow(i,cnt)
r=sorted(list(st))
res=0
for cur in r:
    if cur>B:break
    if A<=cur<=B:
        res+=1
print(res)