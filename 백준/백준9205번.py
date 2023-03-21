def bfs(sj, si, ej, ei):
    # q를 생성, 필요변수 등을 생성!
    q = []
    v = [0] * n

    # q에 초기데이터를 삽입, si, sj는 v에 표시하지 않는다!
    q.append((sj, si))

    while q:
        cj, ci = q.pop(0)
        # 현재 위치에서 목적지의 거리가 1000이내라고 하면
        # 목적지 도달 가능!!
        if abs(cj-ej) + abs(ci-ei) <= 1000:
            return 'happy'

        # 방문하지 않은 모든 편의점 좌표가 범위 내 인지 체크!!
        for i in range(n):
            # 방문하지 않은 편의점!
            if v[i] == 0:
                nj, ni = lst[i]
                if abs(cj-nj) + abs(ci-ni) <= 1000:
                    q.append((nj, ni))
                    v[i] = 1

    return 'sad'


tc = int(input())
for _ in range(tc):
    n = int(input())
    sj, si = map(int, input().split())
    lst = []
    for _ in range(n):
        tj, ti = map(int, input().split())
        lst.append((tj, ti))
    ej, ei = map(int, input().split())

    ans = bfs(sj, si, ej, ei)
    print(ans)
