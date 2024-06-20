import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N=int(input())
a=[input() for _ in range(N)]
res=0
def swap_word(c,c2,s):
    temp=""
    for i,cur in enumerate(s):
        if cur==c:
            temp+=c2
        elif cur==c2:
            temp+=c
        else:
            temp+=cur
    return temp
for i in range(N):
    for j in range(i+1,N):
        s1,s2=a[i],a[j]
        for k in range(len(s1)):
            if s1[k]!=s2[k]:
                s2=swap_word(s1[k],s2[k],s2)
        if s1==s2:
            res+=1

print(res)