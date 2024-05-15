def solution(people, limit):
    answer = 0
    left=0
    right=len(people)-1
    people.sort()
    while left<=right:
        if people[left]<=limit-people[right]:
            left+=1
        right-=1
        answer+=1
    return answer