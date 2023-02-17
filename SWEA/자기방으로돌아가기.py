t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # 복도배열 만들어주기!
    cnts = [0] * 200
    ans = 0
    for _ in range(n):
        start, end = map(int, input().split())
        # 출발지점이 도착지점번호보다 클경우!
        if start > end:
            start, end = end, start
        for i in range((start - 1) // 2, (end - 1) // 2 + 1):
            cnts[i] += 1

    for i in range(len(cnts)):
        if ans < cnts[i]:
            ans = cnts[i]
    print(f'#{tc} {ans}')