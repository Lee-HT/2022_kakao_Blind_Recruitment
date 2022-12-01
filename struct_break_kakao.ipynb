def dsum(r1,c1,r2,c2,degree):       #가로와 세로의 누적합 한번에 처리
    global acsum
    acsum[r1][c1] += degree
    acsum[r1][c2] -= degree
    acsum[r2][c1] -= degree
    acsum[r2][c2] += degree

def Sum(atype,r1,c1,r2,c2,degree):
    r2 += 1
    c2 += 1
    if atype == 2:                 #회복일 시 그대로 입력
        dsum(r1,c1,r2,c2,degree)
    else:                          #공격일 시 -후 입력
        dsum(r1,c1,r2,c2,-degree)

def res_sum(H,W):
    global acsum
    for h in range(H):         #세로로 누적합 계산
        s = 0                  #이전 값
        for w in range(W):
            n = acsum[h][w]    #현재 값
            n = s + n
            acsum[h][w] = n
            s = n
    for w in range(W):         #가로로 누적합 계산
        s = 0
        for h in range(H):
            n = acsum[h][w]
            n = s + n
            acsum[h][w] = n
            s = n
    
def fin_sum(board,H,W,acsum):
    answer = 0
    for h in range(H):
        for w in range(W):
            board[h][w] += acsum[h][w]     #기존 보드 상태에 공격과 회복량을 +
            if board[h][w] > 0:            #0초과시 정답 추가
                answer += 1
    return answer
           
    
acsum = []

def solution(board, skill):
    global acsum
    H = len(board)
    W = len(board[0])
    acsum = [[0 for j in range(W+1)] for i in range(H+1)]
    
    for s in skill:
        Sum(s[0],s[1],s[2],s[3],s[4],s[5])
        
    res_sum(H,W)
    answer = fin_sum(board,H,W,acsum)
    return answer
