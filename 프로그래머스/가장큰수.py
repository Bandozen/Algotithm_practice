def solution(numbers):

    numbers = [str(i) for i in numbers]
    num_list = []
    for i in numbers:
        if len(i) == 4:
            num_list.append([i, i*3])
        if len(i) == 3:
            num_list.append([i, i*4])
        if len(i) == 2:
            num_list.append([i, i*6])
        if len(i) == 1:
            num_list.append([i, i*12])

    num_list.sort(key=lambda x: x[1], reverse=True)

    # print(num_list)
    answer = []
    for i in num_list:
        answer.append(i[0])

    if answer[0] == '0':
        return '0'
    else:
        return ''.join(answer)


numbers = [0, 0, 0, 0]
print(solution(numbers))
