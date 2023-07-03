import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
s=input()
st=[]
for cur in s:
    while st and st[-1]<cur and M:
        M-=1
        st.pop()
    st.append(cur)

while M:
    M-=1
    st.pop()
print(''.join(st))