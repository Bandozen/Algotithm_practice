def solution(sizes):
    return max(max(i) for i in sizes) * max(min(i) for i in sizes)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))