def solution(brown, yellow):
    answer = []
    N=brown+yellow
    for i in range(1,N):
        if not N%i:
            j=N//i
            y=(j-2)*(i-2)
            b=N-y
            if b==brown and y==yellow:
                return [j,i]
    return answer