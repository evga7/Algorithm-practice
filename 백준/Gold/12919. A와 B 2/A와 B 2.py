import sys
def input():return sys.stdin.readline().rstrip()
s=input()
s2=input()
st=set()
def go(s,s2):
    if s==s2:
        print(1)
        exit(0)
    if s2[-1]=='A' and len(s2)-1>=len(s):
        go(s,s2[:len(s2)-1])
    if s2[0]=='B' and len(s2)-1>=len(s):
        go(s,s2[1:][::-1])
res=go(s,s2)

print(0)