import sys
import re
def input(): return sys.stdin.readline().rstrip()
s=input()
print("SUBMARINE" if re.fullmatch('((100+1+)|01)+',s) else "NOISE")