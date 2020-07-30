n = int(input())
round = []
rank_russian = []
rank_korean = []

for i in range(n):
    round.append(int(input()))
    rank_russian.append(list(map(int,input().split())))
    rank_korean.append(list(map(int,input().split())))



for i in range(n):
    chksm = 0
    russian = sorted(rank_russian[i])
    korean = sorted(rank_korean[i])
    for j in russian:
        #print("russ origin",russian)
        tmp = chksm
        #print("russ:",j)
        for k in korean:
            #print("kor origin",korean)
            #print("kor:",k)
            if j <= k:
                chksm += 1
                #print("del:",j,k)
                #russian.remove(j)
                korean.remove(k)
                break
            else:
                continue
        if chksm == tmp:
            # russian always win
            #print("russ win",j,k)
            #russian.remove(j)
            korean.remove(min(korean))
    print(chksm)
