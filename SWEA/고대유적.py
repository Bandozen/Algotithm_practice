def count(arr):
    maxV = 0
    for i in arr:
        cnt = 0
        for j in i:
            if j == 1:
                cnt+=1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0
    return maxV
        

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_t = list(map(list, zip(*arr)))
    a = count(arr)
    b = count(arr_t)
    if a < b:
        a = b
    print(f'#{tc} {a}')
