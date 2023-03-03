t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0     # 도착한 사람의 수
    ans = 'Possible'
    for i in sorted(arr):
        cnt += 1
        if cnt > i // m * k:
            ans = 'Impossible'
            break
    
    print(f'#{tc} {ans}')