from collections import deque
import sys


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(d[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= maxV and not d[nx]:
                d[nx] = d[x] + 1
                q.append(nx)


maxV = 100000
d = [0] * (maxV + 1)
n, k = map(int, sys.stdin.readline().split())

bfs()
