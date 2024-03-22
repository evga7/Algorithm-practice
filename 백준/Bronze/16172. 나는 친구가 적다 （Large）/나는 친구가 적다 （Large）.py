import sys
def input():
    return sys.stdin.readline().rstrip()
s=input()
s2=input()
idx=0
def kmp(all_string, pattern):
    #  kmp_table
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]

        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i

    #  kmp
    result = []
    i = 0
    for j in range(len(all_string)):
        if all_string[j].isdigit():continue
        while i > 0 and pattern[i] != all_string[j]:
            i = table[i-1]

        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                return 1

    return 0

print(kmp(s,s2))