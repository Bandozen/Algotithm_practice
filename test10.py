divs = [2, 3, 5, 7, 11]
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [0] * len(divs)

    for i in range(len(divs)):
        while n % divs[i] == 0:
            lst[i] += 1
            n = n // divs[i]

    print(f'#{tc}', *lst)