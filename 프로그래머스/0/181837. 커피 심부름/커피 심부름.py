def solution(order):
    answer = 0
    for cur in order:
        if "americano" in cur or cur=="anything":
            answer+=4500
        elif "cafelatte" in cur:
            answer+=5000
        
    return answer