import heapq
n = int(input())

q = []
for i in range(n):
    n1, n2 = map(int, input().split())
    heapq.heappush(q, (n1, n2))

start, end = heapq.heappop(q)
answer = 0
while q:
    n1, n2 = heapq.heappop(q)
    if n1 <= end:
        end = max(end, n2)
    else:
        answer += end-start
        start = n1
        end = n2
print(answer+end-start)