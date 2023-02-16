import sys

n = int(input())
m = []
for i in range(n):
    m.append(int(sys.stdin.readline()))
m.sort()
for j in m:
    print(j)