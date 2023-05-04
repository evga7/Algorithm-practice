from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
S=input()
st=set()
m=defaultdict(str)
v=[]
def go(ss,l,r,sts):
    if ss==S:
        st.add(sts)
        return
    if len(ss)>=len(S):
        return
    if l-1>=0:
        go(S[l-1]+ss,l-1,r,sts+S[l-1:r+1])
    if r+1<len(S):
        go(ss+S[r+1],l,r+1,sts+S[l:r+2])
for i,cur in enumerate(S):
    go(S[i],i,i,S[i])
print(len(st))