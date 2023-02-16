from pprint import pprint
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr1 = [list(map(int, input().split())) for _ in range(n)]
    pprint(arr1)
    arr2 = []
    maxV = 0
    for i in range(1, n):
        for j in range(n-m+1):
            arr2.append(arr1[i-1][j:j+m])
            arr2.append(arr1[i][j:j+m])
    pprint(arr2[0])
    