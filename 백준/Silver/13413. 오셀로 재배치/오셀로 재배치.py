T=int(input())
def chk():
    cnt=0
    w_cnt=0
    b_cnt=0
    for i in range(N):
        if s[i]==s2[i]:continue
        if s2[i]=='W':
            if b_cnt:
                b_cnt-=1
                cnt+=1
            else:
                w_cnt+=1
        elif s2[i]=='B':
            if w_cnt:
                w_cnt-=1
                cnt+=1
            else:
                b_cnt+=1
            
    return cnt+w_cnt+b_cnt
        
        
            
while T:
    T-=1
    N=int(input())
    s=list(input())
    s2=list(input())
    print(chk())
    