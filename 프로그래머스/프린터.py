def solution(priorities, location):
    answer = 0
    while True:
        maxV = max(priorities)  # 먼저 리스트에서 가장 큰 수를 구해줍니다.
        for i in range(len(priorities)): # 주어진 배열의 길이만큼 반복문을 돌려서
            if maxV == priorities[i]: # 만약 최댓값이 i번째 원소와 같다면
                answer += 1 # 프린트 한것이 맞으므로 answer에 1 추가
                priorities[i] = 0 # 프린트한 것은 0으로 표시
                maxV = max(priorities) # 다시 최댓값 설정해주기!
                if i == location: # 만약 location 과 일치하면 그대로 answer를 반환!
                    return answer

priorities = [2, 1, 3, 2]
location = 2

print(solution(priorities, location))