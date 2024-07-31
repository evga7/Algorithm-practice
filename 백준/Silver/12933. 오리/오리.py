import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
s=input()
ss="quack"
res=0
cnt=0
visited=[0 for _ in range(len(s))]
def go(start):
    global cnt,res
    idx=0
    for i in range(start,len(s)):
        cur=s[i]
        if cur == ss[idx] and not visited[i]:
            visited[i] = 1
            idx += 1
            cnt += 1
            if idx == 5:
                idx = 0
    if cnt % 5:
        print(-1)
        exit(0)
    res+=1
for i in range(len(s)):
    if not visited[i] and s[i]=='q':
        go(i)
if cnt!=len(s):
    res=-1
print(res)