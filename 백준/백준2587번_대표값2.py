arr = []
for i in range(5):
    arr.append(int(input()))
average = 0
med = 0
average = sum(arr) / len(arr)
arr = sorted(arr)
for i in range(len(arr)):
    med = arr[2]
print(int(average))
print(med)