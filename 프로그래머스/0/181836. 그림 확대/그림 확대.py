def solution(picture, k):
    answer = []
    N=len(picture)
    M=len(picture[0])
    for i in range(N):
        s=""
        for j in range(M):
            s+=picture[i][j]*k
        for l in range(k):
            answer.append(s)
    return answer