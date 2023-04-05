def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        a=bin(arr1[i]|arr2[i])[2:]
        a=a.replace('0',' ')
        a=a.replace('1','#')
        if n>len(a):
            a=' '*(n-len(a))+a
        answer.append(a)
    return answer