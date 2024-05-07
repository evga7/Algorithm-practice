def solution(arr, divisor):
    arr.sort()
    answer=[]
    for cur in arr:
        if not cur%divisor:
            answer.append(cur)
    if not answer:
        answer=[-1]
    return answer