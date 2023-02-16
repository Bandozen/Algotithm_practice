import sys
n = int(sys.stdin.readline().rstrip())
rows, columns, cross = [0] * n, [0] * (2*n-1), [0] * (2*n-1)
answer = 0
def backtracking(r):
    global answer
    if r == n:
        answer += 1
        return
    else:
        for i in range(n):
            can_place = True
            if not (rows[i] or columns[r+i] or cross[r-i+n-1]):
                rows[i] = columns[r+i] = cross[r-i+n-1] = 1
                backtracking(r+1)
                rows[i] = columns[r+i] = cross[r-i+n-1] = 0

backtracking(0)
print(answer)