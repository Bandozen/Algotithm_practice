from collections import deque
import sys
input = sys.stdin.readline

# 먼저 시계 방향으로 설정 북, 동, 하, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 시작지점을 방문체크해주고 카운트 한다!
visited[r][c] = 1
cnt = 1

while True:
    # 아직 청소 시작 안했음!
    flag = 0
    for _ in range(4):
        # 왼쪽 방향부터 한 칸 돌린다!! 요것이 포인트
        d = (d+3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        # 범위 안에 들고, 빈 칸이고, 청소가 가능하다면
        # 돌려서 청소하고, 카운트 하고, 현재 위치를 갱신하고, flag도 변경!
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                r = nr
                c = nc
                # 청소 했다는 뜻
                flag = 1
                break
    # 만약 for문에 안돌아갔을때
    if flag == 0:
        # 네 방향 모두가 청소를 할 수 없을 때와
        # 후진했을 때 벽이면 break!
        # 만약에 후진했는데 벽이 아니라면 그 위치로 다시 갱신해준다!
        if arr[r-dr[d]][c-dc[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dr[d], c-dc[d]
