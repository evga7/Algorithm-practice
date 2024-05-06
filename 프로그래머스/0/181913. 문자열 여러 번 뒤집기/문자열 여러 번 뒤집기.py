def solution(my_string, queries):
    answer = ''
    for cur in queries:
        s,e=cur[0],cur[1]
        my_string=my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]
    return my_string