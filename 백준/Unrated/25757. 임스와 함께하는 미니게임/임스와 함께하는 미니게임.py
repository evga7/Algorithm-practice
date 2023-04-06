import sys
def input():return sys.stdin.readline().rstrip()
N,M=input().split()
N=int(N)
st=set()
m={'Y':2,'F':3,'O':4}
cnt=1
res=0
for i in range(N):
    s=input()
    if not s in st:
        st.add(s)
        cnt+=1
    if m[M]<=cnt:
        res+=1
        cnt=1
print(res)