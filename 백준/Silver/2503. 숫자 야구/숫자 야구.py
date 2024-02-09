import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
def ck(s1,s2):
    s_cnt=0
    b_cnt=0
    st1=set(s1)
    st2 = set(s2)
    for i in range(3):
        if s1[i]==s2[i]:
            s_cnt+=1
            st1.remove(s1[i])
            st2.remove(s1[i])
    for cur in st1:
        if cur in st2:
            b_cnt+=1
    return (s_cnt,b_cnt)
stt=set()
for i in range(123,988):
    ss = str(i)
    if ss[0] == ss[1] or ss[1] == ss[2] or ss[0]==ss[2] or ss.find('0')>=0: continue
    stt.add(i)
for cur in a:
    st,S,B=str(cur[0]),cur[1],cur[2]
    for i in range(123,988):
        ss=str(i)
        if ss[0]==ss[1] or ss[1]==ss[2] or ss[0]==ss[2] or ss.find('0')>=0:continue
        if i in stt and not ck(ss,st)==(S,B) :
            stt.remove(i)
print(len(stt))