import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
s=input()
res=s.count('R')
l=len(s)
l_c=[]
r_c=[]
cnt=0
for cur in s:
    if cur=='K':
        cnt+=1
    else:
        l_c.append(cnt)
cnt=0
for cur in s[::-1]:
    if cur=='K':
        cnt+=1
    else:
        r_c.append(cnt)
r_c.reverse()
left=0
right=len(r_c)-1
while left<=right:
    res=max(res,right-left+1+min(l_c[left],r_c[right])*2)
    if l_c[left]>r_c[right]:
        right-=1
    else:
        left+=1
print(res)