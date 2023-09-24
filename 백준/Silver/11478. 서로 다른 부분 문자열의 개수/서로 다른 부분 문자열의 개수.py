import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
s=input()
st=set()
for i in range(len(s)):
    ss=""
    for j in range(i,len(s)):
        ss+=s[j]
        st.add(ss)
print(len(st))