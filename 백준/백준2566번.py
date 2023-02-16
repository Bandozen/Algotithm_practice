arr = []
maxV = 0
x = 0
y = 0
for i in range(9):
    i = list(map(int, input().split()))
    arr.append(i)

for i in range(9):
    for j in range(9):
        if maxV <= arr[i][j]:
            maxV = arr[i][j]
            x = i+1
            y = j+1

print(maxV)
print(x, y)