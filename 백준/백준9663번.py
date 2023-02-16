import sys
def check(x):
    for i in range(x):
        if board[i] == board[x] or abs(x - i) == abs(board[x] - board[i]):
            return False
    return True

def queen(x):
    global answer
    if x == n:
        answer += 1
        return
    else:    
        for i in range(n):
            board[x] = i
            if check(x):
                queen(x + 1)


n = int(sys.stdin.readline().rstrip())
board = [0] * n
answer = 0
queen(0)
print(answer)