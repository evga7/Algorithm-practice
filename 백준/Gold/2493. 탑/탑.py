import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
arr=list(map(int,input().split()))
st=[]
res_v=[]
for i,cur in enumerate(arr):
    while st and arr[st[-1]]<cur:
        st.pop()
    if st:
        res_v.append(st[-1]+1)
    else:
        res_v.append(0)
    st.append(i)
print(*res_v)