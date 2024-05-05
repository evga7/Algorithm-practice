def solution(rank, attendance):
    answer = 0
    v=[]
    for i in range(len(rank)):
        if attendance[i]==True:
            v.append((rank[i],i))
    v.sort()
    return v[0][1]*10000+v[1][1]*100+v[2][1]