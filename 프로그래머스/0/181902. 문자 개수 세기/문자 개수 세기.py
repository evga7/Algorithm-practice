def solution(my_string):
    answer = [0 for _ in range(52)]
    for cur in my_string:
        if cur.islower():
            answer[26+ord(cur)-ord('a')]+=1
        else:
            answer[ord(cur)-ord('A')]+=1
    return answer