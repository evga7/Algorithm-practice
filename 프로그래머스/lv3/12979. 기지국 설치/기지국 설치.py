def solution(n, stations, w):
    answer = 0
    pos=1
    l=w*2+1
    for cur in stations:
        answer+=(cur-w-pos+l-1)//l
        pos=cur+w+1
    if pos<=n:
        answer+=(n-pos+l)//l
    return answer