def solution(M, N):
    answer = 0
    if N<M:
        N,M=M,N
    answer=N-1+(N*(M-1))
    return answer