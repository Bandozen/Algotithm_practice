def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        d = array[a-1:b]
        d.sort()
        answer.append(d[c-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))