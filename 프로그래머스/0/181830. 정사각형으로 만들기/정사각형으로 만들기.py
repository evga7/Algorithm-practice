def solution(arr):
    answer = []
    N=len(arr)
    M=len(arr[0])
    for i in range(N):
        if N>M:
            answer.append(arr[i]+([0]*(N-M)))
        else:
            answer.append(arr[i])
    if N<M:
        for i in range(M-N):
            answer.append([0]*M)
    return answer