import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
T=int(input())
while T:
    T-=1
    N=int(input())
    s=list(input())
    s2 = list(input())
    w_cnt=0
    b_cnt=0
    for i in range(len(s)):
        if s[i]!=s2[i]:
            if s2[i]=='W':
                w_cnt+=1
            else:
                b_cnt+=1
    print(max(w_cnt,b_cnt))