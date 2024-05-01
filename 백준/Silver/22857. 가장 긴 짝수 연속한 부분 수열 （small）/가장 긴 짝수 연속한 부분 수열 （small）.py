import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N,M=map(int,input().split())
a=list(map(int,input().split()))
left=0
right=0
o_cnt=0
e_cnt=0
res=0
while right<N:
    if a[right]&1:
        o_cnt+=1
    else:
        e_cnt+=1
    while o_cnt>M:
        if a[left]&1:
            o_cnt-=1
        else:
            e_cnt-=1
        left+=1
    res = max(res, e_cnt)
    right+=1
print(res)