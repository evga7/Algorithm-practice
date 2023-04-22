import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
st=[]
st.append(0)
a=[list(map(int,input().split())) for _ in range(N)]
a.sort()
res=0
for cur in a:
    h=cur[1]
    while st and st[-1]>h:
        res+=1
        st.pop()
    if st and st[-1]==h:continue
    st.append(h)
while st:
    if st[-1]>0:
        res+=1
    st.pop()
print(res)