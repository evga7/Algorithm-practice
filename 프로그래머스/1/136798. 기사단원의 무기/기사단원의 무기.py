import math
def solution(number, limit, power):
    answer = 1
    for i in range(2, number + 1):
        cnt = 2
        for j in range(2, int(math.sqrt(i)) + 1):
            if not i % j:
                cnt += 1
                if j<i//j:
                    cnt+=1
                if cnt > limit:
                    break

        if cnt <= limit:
            answer += cnt
        else:
            answer += power
    return answer