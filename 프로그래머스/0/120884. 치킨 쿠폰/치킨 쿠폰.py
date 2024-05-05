def solution(chicken):
    answer = 0
    while chicken>=10:
        num=chicken//10
        c=chicken%10
        answer+=num
        chicken//=10
        chicken+=c
    return answer