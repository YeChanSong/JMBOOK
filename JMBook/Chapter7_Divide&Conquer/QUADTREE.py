import sys
sys.setrecursionlimit(sys.getrecursionlimit())

def recur(qt):
    # 기저사례, b,w인 경우
    if len(qt) == 1:
        return qt[0]
    # 기저사례가 아닌 경우 == 첫 부분 x인 경우
    # 따라서 시작 인덱스를 1로 둔다.
    i = 1
    # 4개로 분할 할 영역을 담을 DQ리스트와 인덱스 dq
    DQ = ['','','','']
    dq = 0
    # 전체 문자열을 4분할 할 것이므로 문자열 전체를 순회한다.
    while i < len(qt):
        if qt[i] == 'x':
            # x가 나온 경우, x뒤에 붙는 알파벳을 확인할 만큼 반복횟수를 늘려야한다.
            # tmp: x뒤로 오는 알파벳을 확인하기 위한 반복횟수. x가 더이상 없다고 가정하고 4로 둔다.
            # xcnt: x의 수. x 뒤에 붙는 알파벳의 수는 4x+1인데, 이를 계산하기 위함.
            # jcnt: x로부터 진행한 수. x뒤에 또 x가 나오는 경우 그만큼 tmp값을 늘려줘야 하는데, 이때 이미 진행한 만큼 빼야한다. 뺄셈을 위한 변수.
            tmp = 4
            jcnt = 1
            xcnt = 1
            
            for j in range(i+1,len(qt)):
                # x부터 뒤쪽으로 순회하며 4분할 할 문자열의 길이를 계산
                jcnt +=1
                if tmp == 0:
                    break
                if qt[j] != 'x':
                    tmp -= 1
                else:
                    xcnt += 1
                    tmp = xcnt*4 + 1 - jcnt
                    # 원래 분할될 문자열의 길이는 4x+1이고, 현재까지 진행한 위치값인 jcnt를 빼서 확인할 문자열의 길이를 계산
	        
            # 분할한 문자열을 DQ배열에 저장하고 인덱스 i의 값을 4x+1만큼 증가시킨다.
            DQ[dq] = qt[i:i+xcnt*4+1]
            dq += 1
            i += xcnt*4 + 1
        else:
		  	# x가 아닌 문자열의 경우 DQ에 저장하고 인덱스를 한칸 옮긴다.
            DQ[dq] = qt[i]
            dq += 1
            i += 1
    
    # 4분할 한 문자열을 뒤집는 순서대로 연결하여 반환한다.
    return qt[0] + recur(DQ[2]) + recur(DQ[3]) + recur(DQ[0]) + recur(DQ[1])


C = int(input())
for i in range(C):
    qt = input()
    print(recur(qt))