def solution(scores):
    answer = 1
    w=scores[0]
    p=sum(w)
    scores.sort(key=lambda x:(-x[0],x[1]))
    b=scores[0][1]
    for cur in scores:
        if cur[0]>w[0] and cur[1]>w[1]:
            return -1
        if b<=cur[1]:
            b=cur[1]
            if p<cur[0]+cur[1]:
                answer+=1
    return answer