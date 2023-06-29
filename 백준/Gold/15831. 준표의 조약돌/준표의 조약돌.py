import sys
def input(): return sys.stdin.readline().rstrip()
N,B,W=map(int,input().split())
s=input()
b_cnt=0
w_cnt=0
left=0
right=0
res=0
while True:
    if b_cnt<=B and w_cnt>=W:
        res=max(right-left,res)
    else:
        while b_cnt>B and left<right:
            if s[left]=='W':
                w_cnt-=1
            else:
                b_cnt-=1
            left+=1
    if right>=N:
        break
    if s[right] == 'W':
        w_cnt += 1
    else:
        b_cnt += 1

    right+=1

print(res)