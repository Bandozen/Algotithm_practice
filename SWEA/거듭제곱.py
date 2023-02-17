for tc in range(10):
    t = int(input())
    a, b = map(int, input().split())
    num = 1
    for _ in range(b):
        num *= a
    print(f'#{t} {num}')
