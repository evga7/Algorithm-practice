def solution(n, s):
    if s<n:
        return [-1]
    answer = []
    a=s//n
    for i in range(n):
        answer.append(a)
    if s%n:
        s-=a*n
        for i in range(n):
            if not s:break
            answer[i]+=1
            s-=1
    answer.sort()
    return answer