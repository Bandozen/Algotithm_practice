T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cnts = [0] * 1001
    for i in range(N):
        bus, S, E = map(int, input().split())
        if bus == 1:
            cnts[S] += 1
            cnts[E] += 1
            while S < E:
                S += 1
                if S != E:
                    cnts[S] += 1

        elif bus == 2:
            cnts[S] += 1
            cnts[E] += 1

            if S % 2 == 0:
                while S < E:
                    S += 2
                    if S != E:
                        cnts[S] += 1

            elif S % 2 == 1:
                while S < E:
                    S += 2
                    if S != E:
                        cnts[S] += 1

        elif bus == 3:
            cnts[S] += 1
            cnts[E] += 1

            if S % 2 == 0:
                while S < E and S != E:
                    S += 2
                    if S % 4 == 0 and S != E:
                        cnts[S] += 1

            elif S % 2 == 1:
                while S < E:
                    S += 1
                    if S % 3 == 0 and S % 10 != 0 and S != E:
                        cnts[S] += 1

    print(f'#{test_case}', max(cnts))
