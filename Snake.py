import random
import pprint

def main():
    board = initialize_board()
    snake, snake_len = initialize_snake(board)
    depth = random.randint(1,20)
    moves = check_moves(snake, board, snake_len,depth)

    print('Number of possible paths:', moves)

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
    return snake,snake_len

def check_moves(snake, board, snake_len,depth):
    moves = 0 
    more_moves = True
    while(more_moves):
        while(depth >= moves):
            moves += 1

            check_up(snake, snake_len)

def check_up(snake, snake_len):
    new_snake = {}
    if snake[0]['row']>=0:
        more_moves = True
        for i in range(snake_len):
            if i ==0:
                new_snake[i] = {"row": snake[0]['row']-1,
                    "column": snake[0]['column']}
            else:
                new_snake[i] = snake[i+1]
    else:
        more_moves = False
    
    return more_moves,new_snake

def check_down(snake, board, snake_len):
    new_snake = {}
    if snake[0]['row']<= board[1]:
        more_moves = True
        for i in range(snake_len):
            if i ==0:
                new_snake[i] = {"row": snake[0]['row']+1,
                    "column": snake[0]['column']}
            else:
                new_snake[i] = snake[i+1]
    else:
        more_moves = False
    
    return more_moves, new_snake

def check_left(snake, snake_len):
    new_snake = {}
    if snake[0]['column']>=0:
        more_moves = True
        for i in range(snake_len):
            if i ==0:
                new_snake[i] = {"row": snake[0]['row'],
                    "column": snake[0]['column']-1}
            else:
                new_snake[i] = snake[i+1]
    else:
        more_moves = False
    
    return more_moves,new_snake

def check_rigth(snake, board, snake_len):
    new_snake = {}
    if snake[0]['column']<= board[0]:
        more_moves = True
        for i in range(snake_len):
            if i ==0:
                new_snake[i] = {"row": snake[0]['row'],
                    "column": snake[0]['column']+1}
            else:
                new_snake[i] = snake[i+1]
    else:
        more_moves = False
    
    return more_moves, new_snake

main()
