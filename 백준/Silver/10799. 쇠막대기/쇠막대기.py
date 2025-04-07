import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
s=input()
st=[]
res=0
for i in range(len(s)):
    cur=s[i]
    if cur=='(':
        st.append(cur)
    else:
        if s[i-1]=='(':
            st.pop()
            res+=len(st)
        else:
            res+=1
            st.pop()

print(res)