'''
문제 해결 방법

2차원 리스트 사용 - 값들을 배열에 저장
moves 값에 따른 세로로(열) 값 유무 계산 
    - 0이 아니면 0으로 수정 및 basket 변수에 append
# basket 변수 값 비교 
#     - 오류시 try catch 처리 / count 변수에 2추가
# 끝
'''
# import numpy as np

def solution(board, moves):
    basket = [0] # 0을 넣어두면 if len(basket) > 1: 을 할 필요가 없다
    answer = 0
    # print(np.array(board))

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                
                if basket[-1] == basket[-2]:
                    basket[-2:] = [] # == basket.pop(-1) X 2
                    answer += 2
                break
    return answer