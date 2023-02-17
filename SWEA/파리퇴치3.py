dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cross1 = [-1, -1, 1, 1]
cross2=[-1, 1, -1, 1]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    fly = []
    for i in range(n):
        for j in range(n):
            catch1 = 0
            catch1 += arr[i][j]
            for k in range(4):
                for k2 in range(1, m):
                    nr = i + dr[k] * k2
                    nc = j + dc[k] * k2
                    if 0 <= nr < n and 0 <= nc < n:
                        catch1 += arr[nr][nc]
                        fly.append(catch1)
    for i in range(n):
        for j in range(n):
            catch2 = 0
            catch2 += arr[i][j]
            for l in range(4):
                for l2 in range(1, m):
                    nr2 = i + cross1[l] * l2
                    nc2 = j + cross2[l] * l2
                    if 0 <= nr2 < n and 0 <= nc2 < n:
                        catch2 += arr[nr2][nc2]
                        fly.append(catch2)

    print(f'#{tc} {max(fly)}')
    