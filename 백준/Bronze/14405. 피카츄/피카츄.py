import sys
def input(): return sys.stdin.readline().rstrip()
s=input()
s=s.replace('pi',' ')
s=s.replace('ka',' ')
s=s.replace('chu',' ')
s=s.replace(' ','')
if s:
    print("NO")
else:
    print("YES")