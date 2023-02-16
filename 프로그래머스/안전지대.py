# 패딩을 사용하기위해 numpy 그리고 counter 모듈 임포트해주기!
import numpy as np
from collections import Counter

def solution(board):
    a = len(board)
    # 패딩의 기본 요소
    # np.pad(패딩을 할 배열, 크기 지정, 테두리에 넣을 상수값(기본값은 0))

    # pad함수를 사용해서 주어진 2차원 배열의 상하좌우 1줄씩 -1을 추가한 board_padded를 생성!
    board_padded = np.pad(board, ((1,1), (1,1)), constant_values = -1)
    # 이후에 똑같이 위험한곳을 설정해준다.
    danger = np.pad(board, ((1,1), (1,1)), constant_values = -1)
    # for문은 패딩된자리가 있기때문에 1부터 시작했다.
    for i in range(1, a+1):
        for j in range(1, a+1):
            if board_padded[i][j] == 1:
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        danger[x][y] = 1
    danger_list = danger.reshape(1, -1).squeeze()
    answer = Counter(danger_list)[0]
    return answer