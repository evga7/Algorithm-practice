import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
if N&1:
    res='SK'
else:
    res='CY'
print(res)
