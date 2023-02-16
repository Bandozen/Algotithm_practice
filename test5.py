students = [i for i in range(1,31)]

for n in range(28):
    ck = int(input())
    students.remove(ck)

print(min(students))
print(max(students))