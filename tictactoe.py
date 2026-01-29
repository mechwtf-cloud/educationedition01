EMPTY = WHITE_CONCRETE
PLAYER = RED_CONCRETE
BOT = BLUE_CONCRETE

start_x = 0
start_y = 5
start_z = 0

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

coords = [
    [(start_x, start_y, start_z),     (start_x, start_y, start_z+1),     (start_x, start_y, start_z+2)],
    [(start_x+1, start_y, start_z),   (start_x+1, start_y, start_z+1),   (start_x+1, start_y, start_z+2)],
    [(start_x+2, start_y, start_z),   (start_x+2, start_y, start_z+1),   (start_x+2, start_y, start_z+2)]
]
def start_game():
    
    for i in range(3):
        for j in range(3):
            x, y, z = coords[i][j]
            blocks.place(EMPTY, world(x, y, z))

    player.say("doska hotova")
    


player.on_chat("start", start_game)

def player_move_cmd(num):
    i = num // 3
    j = num % 3

    if board[i][j] != 0:
        player.say("obsadene ")
        return

    board[i][j] = 1
    x, y, z = coords[i][j]
    blocks.place(RED_CONCRETE, world(x, y, z))

    bot_move()

def bot_move():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 2
                x, y, z = coords[i][j]
                blocks.place(BLUE_CONCRETE, world(x, y, z))
                return

player.on_chat("move", player_move_cmd)
