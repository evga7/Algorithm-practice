import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
st=[]
res=[0 for _ in range(N)]
res2=[0 for _ in range(N)]
for i in range(N):
    cur=a[i]
    while st and a[st[-1]]<=cur:
        st.pop()
    res[i]+=len(st)
    if st:
        res2[i]=st[-1]+1
    st.append(i)
st=[]
for i in range(N-1,-1,-1):
    cur=a[i]
    while st and a[st[-1]]<=cur:
        st.pop()
    res[i] += len(st)
    if st:
        if res2[i]:
            if abs(res2[i]-1-i)>abs(st[-1]-i):
                res2[i]=st[-1]+1
        else:
            res2[i]=st[-1]+1
    st.append(i)
for i in range(N):
    if res[i]:
        print(res[i],end=' ')
        print(res2[i])
    else:
        print(0)