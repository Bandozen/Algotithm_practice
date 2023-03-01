t = int(input())
for tc in range(1, t+1):
    n = int(input())
    answer = -1
    for i in range(1, n+1):
        if i * i * i > n:
            break
        if i * i * i == n:
            answer = i
            break
    print(f'#{tc} {answer}')
