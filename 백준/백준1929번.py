# 처음 코드
# a,b = map(int, input().split())
# for i in range(a, b+1):
#     error = 0
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 error+=1
#                 break
#         if error == 0:
#             print(i)

# 수정한 코드
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True

a,b = map(int, input().split())

for i in range(a, b+1):
    if is_prime_number(i):
        print(i)