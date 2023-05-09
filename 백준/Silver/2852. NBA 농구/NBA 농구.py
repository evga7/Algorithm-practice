import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
res1=0
res2=0
s1=0
s2=0
t=0
for i in range(N):
    team,tt=input().split()
    m,s=map(int,tt.split(':'))
    m*=60
    time=m+s
    if s1 > s2:
        res1 += time - t
    elif s1 < s2:
        res2 += time - t
    if team=='1':
        s1+=1
    else:
        s2+=1
    t=time

if s1 > s2:
    res1 += 60*48 - time
elif s1 < s2:
    res2 += 60*48 - time
print('{:0>2}:{:0>2}'.format(res1//60,res1%60))
print('{:0>2}:{:0>2}'.format(res2//60,res2%60))