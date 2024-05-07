def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        c,c2=arr1[i],arr2[i]
        c=bin(c|c2)[2:]
        c=c.rjust(n,"0")
        c=c.replace('1','#')
        c=c.replace('0',' ')
        answer.append(c)
                
    return answer