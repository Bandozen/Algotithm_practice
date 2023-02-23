dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(m):
            cnt = 0
            for d in range(4):
                nr = i + dr[d]
                nc = j + dc[d]
                if 0 <= nr < n and 0 <= nc < n and (arr[i][j] == 1 or arr[j][i] == 1):
                    cnt+=1
            answer.append(cnt)
    print(f'#{tc} {max(answer) - 1}')

    # 집가서 배열회전 하는거 확인하기!
    
