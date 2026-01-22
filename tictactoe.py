EMPTY = WHITE_CONCRETE
PLAYER = RED_CONCRETE
BOT = BLUE_CONCRETE

start_x = 10
start_y = 5
start_z = 10

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

coords = [
    [(start_x,start_y,start_z),(start_x,start_y,start_z+1),(start_x,start_y,start_z+2)],
    [(start_x+1,start_y,start_z),(start_x+1,start_y,start_z+1),(start_x+1,start_y,start_z+2)],
    [(start_x+2,start_y,start_z),(start_x+2,start_y,start_z+1),(start_x+2,start_y,start_z+2)]
]

for i in range(3):
    for j in range(3):
        x,y,z = coords[i][j]
        blocks.place(EMPTY, world(x,y,z))

player.say("DOSKA OK ")

player_move = 4  

i = player_move // 3
j = player_move % 3

if board[i][j] == 0:
    board[i][j] = 1
    x,y,z = coords[i][j]
    blocks.place(RED_CONCRETE, world(x,y,z))

# bot odpovie – prva volna bunka
for bi in range(3):
    for bj in range(3):
        if board[bi][bj] == 0:
            board[bi][bj] = 2
            x,y,z = coords[bi][bj]
            blocks.place(BLUE_CONCRETE, world(x,y,z))
            break
    else:
        continue
    break
