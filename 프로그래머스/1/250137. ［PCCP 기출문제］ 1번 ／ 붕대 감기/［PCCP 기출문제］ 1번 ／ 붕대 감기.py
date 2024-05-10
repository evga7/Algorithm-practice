def heal(health,t,m,h,p,tt):
    c=t//p
    health+=(h*t)+(c*tt)
    return min(m,health)
def solution(bandage, health, attacks):
    answer = health
    cur_t=0
    m=health
    for a_t,dam in attacks:
        ttt=a_t-cur_t
        answer=heal(answer,ttt,m,bandage[1],bandage[0],bandage[2])
        answer-=dam
        if answer<=0:
            return -1
        cur_t=a_t+1
    return answer