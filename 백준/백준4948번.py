def prime_Number(num):
    if num==1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

num_list = list(range(2,246912))
true=[]

for i in num_list:
    if prime_Number(i):
        true.append(i)

n = int(input())
while True:
    cnt = 0
    if n == 0:
        break
    for i in true:
        if n < i <= 2*n:
            cnt += 1
    print(cnt)
    n = int(input())