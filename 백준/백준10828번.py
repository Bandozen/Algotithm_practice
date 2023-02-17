# input으로 받아오면 시간초과 200%!!!
import sys
n = int(sys.stdin.readline())

stack=[]
# n번 동안 명령을 수행하기 위함
for i in range(n):
    command = sys.stdin.readline().split()
    # 각 명령어들마다 해당하는 기능을 넣어주면 된다!
    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])