N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]

for _ in range(K):
    app_x, app_y = map(int, input().split())
    board[app_x - 1][app_y - 1] = 2

T = int(input())
change_x = [0, 1, 0, -1]
change_y = [-1, 0, 1, 0]


def is_collide(y, x):
    if x < 0 or x >= N or y < 0 or y >= N:
        return True
    elif board[y][x] == 1:
        return True
    return False


def change_dir(direction, flag):
    if flag == 'L':
        direction -= 1
        if direction == -1:
            direction = 3
    else:
        direction += 1
        if direction == 4:
            direction = 0
    return direction


counter = 0
x, y = 0, 0
tail_x, tail_y = 0, 0
now_dir = 1
tail_dir = 1
tail_list = []
board[x][y] = 1
for _ in range(T):
    inp_range, input_dir = input().split()
    inp_range = int(inp_range)
    flag = True
    for _ in range(inp_range):
        ny = y + change_y[now_dir]
        nx = x + change_x[now_dir]
        if is_collide(ny, nx):
            flag = False
            break
        else:
            tail_list.append(now_dir)
            if board[ny][nx] != 2:
                board[tail_y][tail_x] = 0
                tail_dir = tail_list.pop(0)
                tail_y += change_y[tail_dir]
                tail_x += change_x[tail_dir]

            board[ny][nx] = 1
            y, x = ny, nx
            counter += 1
    if not flag:
        break
    now_dir = change_dir(now_dir, input_dir)

print(counter + 1)
