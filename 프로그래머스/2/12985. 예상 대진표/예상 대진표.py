def solution(n,a,b):
    answer = 0
    while a!=b:
        mi=min(a,b)
        mx=max(a,b)
        if (mx-mi)==1 and mi&1 and not mx&1:
            break
        a=(a+1)//2
        b=(b+1)//2
        answer+=1

    return answer+1