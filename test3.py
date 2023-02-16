def solution(numbers):
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer

numbers = [1, 2, 3, 4, 5]
print(solution(numbers))