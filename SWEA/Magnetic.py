for tc in range(1, 11):
    n = int(input())
    arr = [map(int, input().split()) for _ in range(n)]
    cnt = 0     # 교착상태 카운트
    # print(arr)
    # 아래로 떨어지기 때문에 열 우선 순회
    for i in list(zip(*arr)):
        prev = 0        # 이전에 숫자
        for j in i:
            if j != 0:
                if j == 2 and prev == 1:
                    cnt += 1
                prev = j
    
    print(f'#{tc} {cnt}')