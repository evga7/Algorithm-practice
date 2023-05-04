import sys
def input():return sys.stdin.readline().rstrip()
s=input()
f1=0
f2=0
for cur in s:
    if cur.isupper():
        f1=1
    if cur=='_':
        f2=1
if (f1 and f2) or s[0].isupper():
    print("Error!")
    exit(0)
res=''
if f1:
    for i in range(0,len(s)):
        if s[i].isupper():
            res+='_'+s[i].lower()
            continue
        res+=s[i]


else:
    fl=0
    for i in range(0,len(s)):
        cur=s[i]
        if s[i]=='_':
            if i-1<0 or i+1>=len(s) or not s[i-1].islower() or not s[i+1].islower():
                print("Error!")
                exit(0)
            f1=1
            continue
        if f1:
            cur=s[i].upper()
            f1=0
        res+=cur
print(res)