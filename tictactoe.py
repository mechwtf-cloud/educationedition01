
EMPTY = WHITE_CONCRETE
PLAYER = RED_CONCRETE
BOT = BLUE_CONCRETE


start = player.position()
start_x = int(start.x)
start_y = int(start.y)
start_z = int(start.z)

board_state = [[0]*3 for _ in range(3)]
coords = [[None]*3 for _ in range(3)]


for i in range(3):
    for j in range(3):
        x = start_x + i
        y = start_y - 1
        z = start_z + j + 1
        coords[i][j] = (x, y, z)
        blocks.place(EMPTY, world(x, y, z))

def check_win(state, mark):

    for i in range(3):
        if state[i][0]==mark and state[i][1]==mark and state[i][2]==mark:
            return True

    for j in range(3):
        if state[0][j]==mark and state[1][j]==mark and state[2][j]==mark:
            return True
 
    if state[0][0]==mark and state[1][1]==mark and state[2][2]==mark:
        return True
    if state[0][2]==mark and state[1][1]==mark and state[2][0]==mark:
        return True
    return False


def check_draw(state):
    draw = True
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                draw = False
    return draw


def find_cell(x, y, z):
    for i in range(3):
        for j in range(3):
            cx, cy, cz = coords[i][j]
            if int(cx)==int(x) and int(cy)==int(y) and int(cz)==int(z):
                return i, j
    return None


def bot_move():
    for i in range(3):
        for j in range(3):
            if board_state[i][j]==0:
                board_state[i][j]=2
                cx, cy, cz = coords[i][j]
                blocks.place(BOT, world(cx, cy, cz))
                return


while True:
    pos = player.position()
    foot_x = int(pos.x)
    foot_y = int(pos.y-1)
    foot_z = int(pos.z)

    cell = find_cell(foot_x, foot_y, foot_z)
    if cell:
        i, j = cell
        if board_state[i][j]==0:
            board_state[i][j]=1
            blocks.place(PLAYER, world(foot_x, foot_y, foot_z))

            if check_win(board_state,1):
                break

            bot_move()
            if check_win(board_state,2):
                break

            if check_draw(board_state):
                break

    loops.pause(200)
