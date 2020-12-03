import sys
sys.setrecursionlimit(sys.getrecursionlimit())

def recur(qtiter):
    
    qt = next(qtiter)
    if qt != 'x':
        return qt
    
    ul = recur(qtiter)
    ur = recur(qtiter)
    ll = recur(qtiter)
    lr = recur(qtiter)
    
    
    return 'x' + ll + lr + ul + ur


C = int(input())
for i in range(C):
    qt = input()
    print(recur(iter(qt)))