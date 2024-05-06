import bisect
def solution(arr, queries):
    answer = []
    for s,e,cur in queries:
        v=arr[s:e+1]
        a=987654321
        for cur2 in v:
            if cur<cur2:
                a=min(a,cur2)
        if a!=987654321:
            answer.append(a)
        else:
            answer.append(-1)
    return answer