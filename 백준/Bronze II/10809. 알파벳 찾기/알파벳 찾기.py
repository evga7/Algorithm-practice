import sys
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
s=input()
a=[-1 for _ in range(26)]
for i in range(len(s)):
    c=ord(s[i])-ord('a')
    if a[c]==-1:
        a[c]=i
print(*a)