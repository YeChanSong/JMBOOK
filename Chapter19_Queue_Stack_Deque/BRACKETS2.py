C = int(input())
# 테스트 케이스 수 입력
left = ['(', '{', '[']
right = [')','}',']']
# 꺽쇠 비교를 위한 left right
li = []
# 스택용으로 사용할 리스트 li
answer = []

for i in range(C):
    init = input()
    li.clear()
    flag = True
    
    for j in init:
        if j in left:
            # 왼쪽 꺽쇠가 나온 경우
            li.append(j)
        elif len(li) == 0 and j in right:
            # 오른쪽 꺽쇠만 나온 경우
            flag = False
            break
        if j in right:
            # 오른쪽 꺽쇠가 나온 경우
            tmp = li.pop()
            if left.index(tmp) == right.index(j):
                continue
            else:
                flag = False
                break
    # flag와 스택에 저장된 원소의 수를 가지고 Yes No 판별
    if flag == True and len(li) == 0:
        answer.append("YES")
    if len(li) > 0 or flag == False:
        # 왼쪽 꺽쇠만 나올 수 있으므로 스택의 크기가 0이 아닌 경우 예외 처리
        answer.append("NO")
        
# 정답 출력
for i in answer:
    print(i)

