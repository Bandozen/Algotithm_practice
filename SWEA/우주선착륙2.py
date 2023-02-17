# 방향탐색
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(m):
            cnt = 0
            for d in range(8):
                nr = i + dr[d]
                nc = j + dc[d]
                if 0 <= nr < n and 0 <= nc < m and arr[i][j] > arr[nr][nc]:
                    cnt += 1
            if cnt >= 4:
                answer += 1
    print(f'#{tc} {answer}')
