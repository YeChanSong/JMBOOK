import sys
from collections import deque

# 시간초과

def bfs(start):
    global cntr, q, discovered, ans
    flag = False
    while len(q) > 0:
        if flag:
            break
        tmp = q.popleft()
        if tmp == '-1':
            cntr+=1
            continue
        itm = ''.join(tmp)
        discovered[int(itm)] = True
        
        
        l = 0
        for i in range(8):
            l+=1
            if l >= len(tmp):
                continue
            for j in range(8):
                if j + l >= len(tmp):
                    break
                ttmp = tmp.copy()
                rev = list(reversed(tmp[j:j+l+1]))
                for k in range(len(rev)):
                    ttmp[j+k] = rev[k]
                a = int(''.join(ttmp))
                #print(itm,a)
                if ans == a:
                    flag = True
                    break
                if discovered.get(a) == None:
                    
                    discovered.setdefault(a,False)
                    q.append(ttmp)
            #print(cntr)
            if flag:
                break
        q.append('-1')

with open('init.txt','r') as f:
    C = int(f.readline().strip())
    for i in range(C):
        N = int(f.readline().strip())
        init = list(f.readline().strip().split())
        ans = int(''.join(sorted(init)))
        li = int(''.join(init))
        cntr = 0
        if li == ans:
            print(cntr)
        else:
            cntr +=1
            discovered = dict()
            discovered.setdefault(li,False)
            q = deque()
            q.append(init)
            q.append('-1')
            bfs(li)
            print(cntr)
        