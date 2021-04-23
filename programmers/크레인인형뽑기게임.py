# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = [0]
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                pass
            else:
                if basket[-1] == board[j][i-1]:
                    answer += 2
                    basket.pop()
                    

                    
                else:
                    basket.append(board[j][i-1])

                board[j][i-1] = 0
                break
            
    return answer
