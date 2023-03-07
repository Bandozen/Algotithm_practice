t = int(input())
stack = []
def dfs(r, c):
    global minV
    if r == n // 2:
        pass
    
for tc in range(1, t+1):
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
    minV = 10000000000   
    dfs(0, 0)
    print(f'#{tc} {minV}')