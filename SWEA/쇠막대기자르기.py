t = int(input())
for tc in range(1, t+1):
    string = input()
    # 막대기 개수
    cnt = 0
    # 자른 횟수
    ans = 0
    for i in range(len(string)):
        # 막대기 혹은 레이저 시작!
        if string[i] == "(":
            cnt += 1
        else:
            # 레이저 시작!
            if string[i-1] == "(":
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1
    
    print(f'#{tc} {ans}')