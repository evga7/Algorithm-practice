import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
st=set()
for i in range(123,988):
    s=str(i)
    if s.count(s[0])>1 or s.count(s[1])>1 or s.count(s[2])>1 or s.count('0')>0:continue
    st.add(i)
for i in range(N):
    num,s,b=map(int,input().split())
    num=str(num)
    for j in range(123,988):
        s_cnt=0
        b_cnt=0
        num2=str(j)
        for k in range(3):
            if num2[k] in num:
                if num2.index(num2[k])==num.index(num2[k]):
                    s_cnt+=1
                else:
                    b_cnt+=1
        if s_cnt==s and b_cnt==b:
            continue
        if j in st:
            st.remove(j)
print(len(st))