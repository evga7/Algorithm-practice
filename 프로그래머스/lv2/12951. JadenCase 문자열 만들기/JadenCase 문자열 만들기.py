def solution(s):
    answer = ''
    a=s.split(' ')
    for i in range(len(a)):
        answer+=a[i].capitalize()+' '
    return answer[:-1]