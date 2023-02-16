t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = cnt = 1
    for i in range(1, n):
        if lst[i] - lst[i-1] != 1:
            cnt = 1
        else:
            cnt += 1
            if ans < cnt:
                ans = cnt
    
    print(f'#{tc} {ans}')