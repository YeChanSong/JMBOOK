# 입력받기
C = int(input())
N = list()
L = list()
cost = list()
for i in range(C):
    n, l = map(int,input().split())
    N.append(n)
    L.append(l)
    cst = list(map(int,input().split()))
    cost.append(cst)

print(cost)
# 각 케이스 계산
for i in range(C):
    low = 1000.0
    for j in range(L[i],N[i]+1):
        # 주어진 비용들을 L부터 N까지 순회하며 최소 평균 구하기
        li = cost[i][:j]
        ptr = j

        while 1:
            #print(li)
            if ptr == len(cost[i]):
                break
			
            tmp = sum(li)/j
            if low > tmp:
                low = tmp
			
            del(li[0])
            #print(ptr)
            
            li.append(cost[i][ptr])
            ptr +=1
    print("%.12f" %low)