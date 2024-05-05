def solution(score):
    answer = []
    v=[]
    l=len(score)
    for i,cur in enumerate(score):
        v.append(cur[0]+cur[1])
    v.sort(reverse=True)
    for cur in score:
        answer.append(v.index(sum(cur))+1)
    return answer