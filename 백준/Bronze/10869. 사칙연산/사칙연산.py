import sys
def input():return sys.stdin.readline().rstrip()
A,B=map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)