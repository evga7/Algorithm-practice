import sys
def input():
    return sys.stdin.readline().rstrip()
s=input()
s2=input()
s3=""
for cur in s:
    if cur.isalpha():
        s3+=cur
if s3.find(s2)>=0:
    print(1)
else:
    print(0)