def solution(arr):
    answer = []
    for cur in arr:
        if answer and answer[-1]==cur:continue
        answer.append(cur)
    return answer