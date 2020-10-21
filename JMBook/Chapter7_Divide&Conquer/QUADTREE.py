import sys
sys.setrecursionlimit(10000000)

def recur(qt):
    
    if len(qt) == 1:
        return qt[0]
    if qt == '':
        return ''
    i = 1
    DQ = ['','','','']
    dq = 0
    while i < len(qt):
        if qt[i] == 'x':
            cnt = 4
            lenstr = 1
            jcnt = 0
            for j in range(i+1,len(qt)):
                jcnt +=1
                if cnt == 0:
                    break
                if qt[j] == 'x':
                    lenstr +=1
                    cnt += 4-jcnt
                else:
                    cnt -= 1
            
            DQ[dq] = qt[i:i+4*lenstr+1]
            dq +=1
            i += 4*lenstr+1
        else:
            
            DQ[dq] = qt[i]
            dq +=1
            i += 1 
    return qt[0] + recur(DQ[2]) + recur(DQ[3]) + recur(DQ[0]) + recur(DQ[1])


C = int(input())
for i in range(C):
    qt = input()
    print(recur(qt))
