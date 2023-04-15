import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
s=input()
r_cnt=0
b_cnt=0
ss=s[::-1]
r_idx=N-ss.find('R')-1
b_idx=N-ss.find('B')-1
res=987654321
for i in range(r_idx):
    if s[i]=='B':
        b_cnt+=1
for i in range(b_idx):
    if s[i]=='R':
        r_cnt+=1
print(min(r_cnt,b_cnt))