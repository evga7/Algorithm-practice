import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
st=set()
right=0
res=0
for left in range(N):
    while right<N and not a[right] in st:
        st.add(a[right])
        right+=1
    res+=right-left
    st.remove(a[left])
print(res)