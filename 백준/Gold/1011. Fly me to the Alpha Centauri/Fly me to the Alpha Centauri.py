import sys
def min_moves(x, y):
    distance = y - x
    k = 1

    while k * (k + 1) < distance:
        k += 1

    if distance <= k * k:
        return 2 * k - 1
    else:
        return 2 * k

# 테스트
N=int(input())
for i in range(N):
    x, y = map(int, input().split())
    print(min_moves(x, y))
