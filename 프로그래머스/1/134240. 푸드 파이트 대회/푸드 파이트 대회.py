def solution(food):
    answer = ''
    s=""
    for i in range(1,len(food)):
        c=food[i]//2
        if c:
            s+=str(i)*c
    return s+'0'+s[::-1]