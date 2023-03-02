grid = [[0] * 1001 for _ in range(1001)]
n = int(input())
for i in range(n):
    x, y, x2, y2 = map(int, input().split())
    for j in range(x, x+x2):
        for k in range(y, y+y2):
            grid[j][k] = i+1

for i in range(n):
    cnt = 0
    for j in grid:
        cnt += j.count(i+1)
    print(cnt)
