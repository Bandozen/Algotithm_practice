def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans1, ans2, ans3 = 0, 0, 0

    for i in range(len(answers)):
        if answers[i] == one[i%5]:
            ans1 += 1
        if answers[i] == two[i%8]:
            ans2 += 1
        if answers[i] == three[i%10]:
            ans3 += 1

    n = max(ans1, ans2, ans3)
    answer = []
    if n == ans1:
        answer.append(1)
    if n == ans2:
        answer.append(2)
    if n == ans3:
        answer.append(3)
        
    return answer

answers = [1,2,3,4,5]
print(solution(answers))