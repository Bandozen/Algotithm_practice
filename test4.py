a = int(input())
b = list(map(int, input().split()))

b.sort()

max_ = b[-1]
min_ = b[0]

print(min_, max_)

cnt = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]

for i in numbers[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min,max)