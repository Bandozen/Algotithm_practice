for tc in range(1, 11):
    a, password = input().split()
    a = int(a)
    stack = []
    real = ''
    for i in password:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    real = ''.join(stack)
    print(f'#{tc} {real}')
