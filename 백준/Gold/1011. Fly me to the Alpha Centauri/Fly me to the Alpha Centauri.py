import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]

def min_steps_to_reach(x, y):
    distance = y - x
    if distance == 0:
        return 0

    # k 값을 증가시키며 최대한 목표에 도달할 수 있는 최소 횟수를 구함
    k = 1
    total_distance = 0
    steps = 0

    while total_distance < distance:
        total_distance += k
        steps += 1
        if total_distance >= distance:
            break
        total_distance += k
        steps += 1
        k += 1

    return steps

# 테스트 케이스 입력
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(min_steps_to_reach(x, y))
