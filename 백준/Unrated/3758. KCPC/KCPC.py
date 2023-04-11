import sys
def input():return sys.stdin.readline().rstrip()
T=int(input())

while T:
    T-=1
    n,k,t,m=map(int,input().split())
    arr=[[False for _ in range(101)] for _ in range(101)]
    sco=[0 for _ in range(101)]
    cnt = [0 for _ in range(101)]
    mx=[0 for _ in range(101)]
    res=1
    a=[]
    for i in range(m):
        q,w,e=map(int,input().split())
        a.append((e,i,w,q))
    a.sort(key=lambda x:(-x[0],x[1]))
    for cur in a:
        score=cur[0]
        seq=cur[1]
        num=cur[2]
        team_id=cur[3]
        cnt[team_id]+=1
        mx[team_id]=max(mx[team_id],seq)
        if not arr[team_id][num]:
            arr[team_id][num]=1
            sco[team_id]+=score
    b=[]
    for i in range(1,n+1):
        b.append((sco[i],cnt[i],mx[i],i))
    b.sort(key=lambda x:(-x[0],x[1],x[2]))
    for cur in b:
        if cur[3]==t:
            break
        res+=1
    print(res)