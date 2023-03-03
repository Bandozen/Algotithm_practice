arr = [['0'] * 101 for _ in range(101)]
n = int(input())
cnt = 0
for _ in range(n):
    a, b = map(int, input().split())
    
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = '1'

for i in arr:
    for j in i:
        if j != '0':
            cnt += 1

print(cnt)