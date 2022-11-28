import copy

def pos_ck(h,w):
    global bh, bw
    clist = []
    if h != 0:
        clist.append((h-1,w))
    if h != bh-1:
        clist.append((h+1,w))
    if w != 0:
        clist.append((h,w-1))
    if w != bw-1:
        clist.append((h,w+1))
        
    return clist

def win_ck(can):
    win = False
    Min = 26
    Max = 0
    
    for c in can:      #상대가 패배하는 루트가 하나라도 존재시 승리 가능
        if c[0]==0:
            win = True
            break
    
    if win: #승
        for c in can:
            if c[0]==0:          #상대가 패배하는 루트 중 이동 횟수가 가장 적은 것 선택
                if c[1] < Min:
                    Min = c[1]
        return (1,Min)    #승리 리턴
    else: #패
        for c in can:            #승리 불가능 -> 이동 횟수가 가장 많은 것 선택
            if c[1] > Max:
                Max = c[1]
        return (0,Max)    #패배 리턴

def move_a(aloc,bloc,move,board):
    if board[aloc[0]][aloc[1]] == 0:     #현재 좌표가 0일시 패배 리턴
        return (0,move)
    clist = pos_ck(aloc[0],aloc[1])    #4방향 좌표 생성
            
    can = []
    for c in clist:
        H,W = c[0],c[1]
        if board[H][W]:      #4방향 각각의 좌표 이동 가능 확인
            board[aloc[0]][aloc[1]] = 0            #현재 a좌표 이동 불가능
            ret = move_b([H,W],bloc,move+1,board)  #B이동 함수로 이동
            can.append(ret)
    board[aloc[0]][aloc[1]] = 1          #다른 루트 탐색을 위한 원상태 복귀
    if can == []:
        return (0,move)      #리스트가 비었을 시 패배 리턴
    else:
        return win_ck(can)   #승리 가능 여부 확인 리턴
    
def move_b(aloc,bloc,move,board):       #move_a를 b로 변형한 함수
    if board[bloc[0]][bloc[1]] == 0:
        return (0,move)
    clist = pos_ck(bloc[0],bloc[1])
    
    can = []
    for c in clist:
        H,W = c[0],c[1]
        if board[H][W]:
            board[bloc[0]][bloc[1]] = 0
            ret = move_a(aloc,[H,W],move+1,board)  #A이동 함수로 이동
            can.append(ret)
    board[bloc[0]][bloc[1]] = 1
    if can == []:
        return (0,move)
    else:
        return win_ck(can)

bh,bw = 0,0
def solution(board, aloc, bloc):
    global bh,bw
    
    bh , bw = len(board), len(board[0])
    ans = move_a(aloc,bloc,0,board)
    answer = ans[1]
    return answer
