import sys
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
s=input()
for cur in s:
    c=cur
    if cur.isalpha():
        if cur.isupper():
            num=ord(cur)+13
            if num>ord('Z'):
                num%=ord('Z')
                num+=ord('A')-1
            c=chr(num)
        else:
            num = ord(cur) + 13
            if num > ord('z'):
                num %= ord('z')
                num += ord('a')-1
            c = chr(num)
    print(c,end='')