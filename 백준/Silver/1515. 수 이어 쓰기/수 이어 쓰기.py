import sys
def input():return sys.stdin.readline().rstrip()
N=input()
s=""
i=0
while True:
    i+=1
    s+=str(i)
    idx=0
    idx2=0
    while idx<len(N) and idx2<len(s):
        if N[idx]==s[idx2]:
            idx+=1
        idx2+=1
    if idx==len(N):
        break
print(i)