MOVES = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}


def move(maze, player, command):
    dr, dc = MOVES[command]
    target = player[0] + dr, player[1] + dc
    return player if maze[target[0]][target[1]] == "#" else target
