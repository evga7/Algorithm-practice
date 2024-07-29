import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
if not N%4 and (N%100 or not N%400):
    print(1)
else:
    print(0)