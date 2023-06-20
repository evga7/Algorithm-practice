import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=set(input() for _ in range(N))
for cur in a:
    r=cur[::-1]
    if cur==r or r in a:
        print(len(cur),cur[len(cur)//2])
        exit(0)