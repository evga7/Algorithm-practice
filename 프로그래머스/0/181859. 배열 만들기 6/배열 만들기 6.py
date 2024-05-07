def solution(arr):
    answer = []
    i=0
    while i<len(arr):
        cur=arr[i]
        if not answer:
            answer.append(cur)
            i+=1
        else:
            if answer[-1]==cur:
                answer.pop()
            else:
                answer.append(cur)
            i+=1
    if not answer:
        answer=[-1]
    return answer