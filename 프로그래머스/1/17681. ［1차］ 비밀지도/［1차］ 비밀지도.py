def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        c,c2=arr1[i],arr2[i]
        c=c|c2
        temp=""
        for j in range(n):
            if c&(1<<j):
                temp+='#'
            else:
                temp+=' '
        answer.append(temp[::-1])
                
    return answer