import sys
sys.setrecursionlimit(sys.getrecursionlimit())

def recur(fence,start,end):
    """
    fence: list
    start, end: index of list
    """
    # 기저사례.
    # 특정한 판자 하나에서 만들 수 있는 직사각형의 넓이 계산
    if start == end:
        tmp = start
        width = 0
        # 판자를 기준으로 왼쪽으로 가능한 넓이
        while 1:
            if tmp < 0:
                break
            if fence[tmp] >= fence[start]:
                width += 1
            else:
                break
            tmp -= 1
        tmp = end
        # 판자를 기준으로 오른쪽으로 가능한 넓이
        while 1:
            if tmp == len(fence):
                break
            if fence[tmp] >= fence[end]:
                width += 1
            else:
                break
            tmp += 1
        # 중복된 기준 판자의 넓이는 빼고 직사각형의 넓이 계산 후 반환
        width -= 1
        return width*fence[start]
    
    return max(recur(fence,start,(start+end)//2),recur(fence,(start+end)//2+1,end))


C = int(sys.stdin.readline().strip())
for i in range(C):
    N = int(sys.stdin.readline().strip())
    height = list(map(int,sys.stdin.readline().strip().split()))
    print(recur(height,0,N-1))
