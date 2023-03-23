def solution(people, limit):
    answer = 0
    people.sort()
    left=0
    N=len(people)
    right=N-1
    while left<=right:
        s=people[right]
        right-=1
        if s+people[left]<=limit:
            left+=1
        answer+=1
    return answer