import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[int(input()) for _ in range(N)]
st=[]
res=0
mn=max(a)
for cur in a:
    if st and st[-1]==cur:continue
    if st and st[-1]<cur:
        res+=cur-st[-1]
    if st:
        st.pop()
    st.append(cur)
res+=mn-st[-1]
print(res)