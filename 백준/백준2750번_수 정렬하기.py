n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
m = sorted(m)
for j in range(len(m)):
    print(m[j])