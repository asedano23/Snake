import random
import pprint

def main():
    board = initialize_board()
    snake = initialize_snake(board)
    depth = random.randint(1,20)


def initialize_board():
    rows = random.randint(1,10)
    columns = random.randint(1,10) 
    board = [rows, columns]

    print ('The board has ', rows, ' rows and ', columns,' columns')
    return board

def initialize_snake(board):
    snake_len = random.randint(3,7)
    snake = {}
    print('The snake has a length of: ', snake_len)
    for len in range(snake_len):
        if len == 0:
            snake_row = random.randint(0,board[1])
            snake_col = random.randint(0,board[1])
        else:
            snake_row = snake_row
            snake_col = snake_col+1

            if snake_row >= board[0]:
               snake_row = snake_row -1
               snake_col = snake_col
            elif snake_row <= board[0]:
                snake_row = snake_row +1
                snake_col = snake_col
            
            if snake_col >= board[0]:
               snake_row = snake_row
               snake_col = snake_col -1
            elif snake_row <= board[0]:
                snake_row = snake_row 
                snake_col = snake_col +1

        snake[len] = {"row": snake_row,
                 "column": snake_col}
    pprint.pprint(snake)
    return snake


main()
