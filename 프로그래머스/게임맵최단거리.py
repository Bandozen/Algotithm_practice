from collections import deque
def solution(maps):
    answer = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def bfs(r,c):
        queue = deque()
        queue.append((r,c))

        while queue:
            r,c = queue.popleft()

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                    queue.append((nr, nc))

        return maps[len(maps)-1][len(maps[0])-1]
    
    answer = bfs(0, 0)
    return -1 if answer == 1 else answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))