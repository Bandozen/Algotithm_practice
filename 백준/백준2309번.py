# 난쟁이들의 키를 담을 배열!
shorts = []
# 입력값들을 받아서 그대로 배열에 넣어줍니다.
for i in range(9):
    shorts.append(int(input()))
# 가짜 난쟁이 2명의 키를 담을 변수 설정
a = 0
b = 0

# 난쟁이 키의 합을 다 더해서 가짜 난쟁이의 키를 빼면 100이니까
# 두 명의 난쟁이들을 고르기 위해 반복문을 두개 돌렸음!
for i in range(len(shorts)):
    for j in range(i+1, len(shorts)):
        if sum(shorts) - (shorts[i] + shorts[j]) == 100:
            a = shorts[i]
            b = shorts[j]

# 그래서 나온 난쟁이들의 키를 배열에서 삭제시켜줍니다.
shorts.remove(a)
shorts.remove(b)
# 정렬을 시킨 다음에
shorts.sort()
# 하나하나 차례씩 프린트해줍니다!
for i in shorts:
    print(i)
