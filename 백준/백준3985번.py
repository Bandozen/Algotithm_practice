# 팬케이크의 길이
l = int(input())
# 사람 수
n = int(input())
# 팬케이크 배열
arr = [0] * l
# 예상 케이크를 받을 방청객 번호
arr2 = []
# 실제 케이크를 받은 방청객 번호
arr3 = []
for people in range(n):
    p, k = map(int, input().split())
    expect = 0
    real = 0
    for i in range(p-1, k):
        expect += 1
        # 여기가 제일 중요!! 이미 값이 있는경우에는 덮어쓰면 안되니까
        # 0인 경우에만 방청객번호를 적어줘야 함!
        # 또한 실제로 받은 케이크 수를 여기서 +1 해줘야 함.
        if arr[i] == 0:
            arr[i] = people+1
            real += 1
    arr2.append(expect)
    arr3.append(real)

maxV = 0
maxV2 = 0
# 인덱스 번호
c1 = 0
c2 = 0
for i in range(len(arr2)):
    if maxV < arr2[i]:
        maxV = arr2[i]
        c1 = i+1
for i in range(len(arr3)):
    if maxV2 < arr3[i]:
        maxV2 = arr3[i]
        c2 = i+1
print(c1)
print(c2)