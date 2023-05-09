import sys
def input():return sys.stdin.readline().rstrip()
while True:
    s=input()
    if s=='*':
        break
    f=0

    for i in range(len(s)-2):
        st = set()
        for j in range(i+1,len(s)):
            ss=s[j-i-1]+s[j]
            if ss in st:
                f=1
                break
            st.add(ss)
        if f:
            break
    print('%s is'%s,end=' ')
    if f:
        print('NOT',end=' ')
    print("surprising.")