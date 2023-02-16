t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input()))
    ans = cnt = 0
    for i in range(n):
        if lst[i] == 0:
            cnt = 0
        else:
            cnt += 1
            if ans < cnt:
                ans = cnt
    
    print(f'#{tc} {ans}')