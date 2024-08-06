import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
arr=list(map(int,input().split()))
st=[]
for i,cur in enumerate(arr):
    while st and arr[st[-1]]<cur:
        st.pop()
    if st:
        print(st[-1]+1,end=' ')
    else:
        print(0,end=' ')
    st.append(i)