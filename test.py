grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
max_score = 0

for i in range(len(grain_lst)):
    if max_score > grain_lst[i][1]:
        max_score = grain_lst[i][1]
    else:
        max_score
print(max_score)
