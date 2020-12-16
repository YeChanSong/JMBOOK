import sys
sys.setrecursionlimit(10000)

def recur(idx):
    global array, cache
    if idx >= len(array):
        return 0
    if cache[idx] != None:
        return cache[idx]
    diff3, diff4, diff5 = 987654321,987564321,987654321
    sub3 = array[idx:idx+3]
    sub4 = array[idx:idx+4]
    sub5 = array[idx:idx+5]
    
    if len(sub3) == 3:
        if sum(sub3) == sub3[0]*3:
            diff3 = 1
        else:
            if (sub3[0] - sub3[1] == sub3[1] - sub3[2] == 1) or (sub3[0] - sub3[1] == sub3[1] - sub3[2] == -1):
                diff3 = 2
            elif sub3[0] == sub3[2]:
                diff3 = 4
            elif abs(sub3[0] - sub3[1]) == abs(sub3[1] - sub3[2]):
                diff3 = 5
            else:
                diff3 = 10
    
    if len(sub4) == 4:
        if sum(sub4) == sub4[0]*4:
            diff4 = 1
        else:
            if (sub4[0] - sub4[1] == sub4[1] - sub4[2] == sub4[2] - sub4[3] == 1) or (sub4[0] - sub4[1] == sub4[1] - sub4[2] == sub4[2] - sub4[3] == -1):
                diff4 = 2
            elif sub4[0] == sub4[2] and sub4[1] == sub4[3]:
                diff4 = 4
            elif abs(sub4[0] - sub4[1]) == abs(sub4[1] - sub4[2]) == abs(sub4[2] - sub4[3]):
                diff4 = 5
            else:
                diff4 = 10
    
    if len(sub5) == 5:
        if sum(sub5) == sub5[0]*5:
            diff5 = 1
        else:
            if (sub5[0] - sub5[1] == sub5[1] - sub5[2] == sub5[2] - sub5[3] == sub5[3] - sub5[4] == 1) or (sub5[0] - sub5[1] == sub5[1] - sub5[2] == sub5[2] - sub5[3] == sub5[3] - sub5[4] == -1):
                diff5 = 2
            elif sub5[0] == sub5[2] == sub5[4] and sub5[1] == sub5[3] :
                diff5 = 4
            elif abs(sub5[0] - sub5[1]) == abs(sub5[1] - sub5[2]) == abs(sub5[2] - sub5[3]) == abs(sub5[3] - sub5[4]):
                diff5 = 5
            else:
                diff5 = 10
    
    tmp = min(recur(idx+3)+diff3, recur(idx+4)+diff4, recur(idx+5)+diff5)
    cache[idx] = tmp
    return tmp


C = int(sys.stdin.readline().strip())
for i in range(C):
    array = list(map(int,sys.stdin.readline().strip()))
    cache = [None for i in range(len(array))]
    ans = recur(0)
    print(ans)