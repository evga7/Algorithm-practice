import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=list(map(int,input().split()))
jun_cnt=0
jun_money=N
sung_cnt=0
sung_money=N
for cur in a:
    if cur<=jun_money:
        j_cnt=jun_money//cur
        jun_cnt+=j_cnt
        jun_money-=cur*j_cnt
for i in range(3,14):
    if a[i-3]<a[i-2]<a[i-1]:
        sung_money+=sung_cnt*a[i]
        sung_cnt=0
    if a[i-3]>a[i-2]>a[i-1]:
        if sung_money>=a[i]:
            s_cnt=sung_money // a[i]
            sung_cnt += s_cnt
            sung_money -= (s_cnt * a[i])
jun_money+=a[13]*jun_cnt
sung_money+=a[13]*sung_cnt
if jun_money>sung_money:
    res="BNP"
elif jun_money<sung_money:
    res="TIMING"
else:
    res="SAMESAME"
print(res)