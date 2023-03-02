n = int(input())
card = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.insert(i - card[i], i+1)

print(*arr)