n = int(input())
a = int(input())
cnt = 0
lst = []
for i in range(n, a+1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error+=1
                break
        if error == 0:
            lst.append(i)

if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)