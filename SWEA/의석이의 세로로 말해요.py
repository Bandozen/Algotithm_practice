t = int(input())
for tc in range(1, t+1):
    arr = [list(input()) + ['']*15 for _ in range(5)]
    string = ''
    for i in range(16):
        for j in range(5):
            string += arr[j][i]
    print(f'#{tc} {string}')
