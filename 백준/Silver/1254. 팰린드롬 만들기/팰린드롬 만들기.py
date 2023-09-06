import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize


def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
s=input()
rs=s[::-1]
res=len(s)-1
for i in range(1,len(rs)):
    rs2=rs[:i+1]
    if rs2==rs2[::-1]:
        res=len(s)-1-i
print(len(s)+res)