MAZE = [
    "#########",
    "#   #   #",
    "# # # # #",
    "# #   # #",
    "# ### #E#",
    "#       #",
    "#########",
]
START = (1, 1)
MOVES = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}


def move(maze, player, command):
    dr, dc = MOVES[command]
    target = player[0] + dr, player[1] + dc
    return player if maze[target[0]][target[1]] == "#" else target


def render(maze, player):
    rows = list(maze)
    row = list(rows[player[0]])
    row[player[1]] = "@"
    rows[player[0]] = "".join(row)
    return "\n".join(rows)


def main():
    player = START
    while MAZE[player[0]][player[1]] != "E":
        print(render(MAZE, player))
        command = input("WASD移动，Q退出：").lower()
        if command == "q":
            return
        if command in MOVES:
            player = move(MAZE, player, command)
    print(render(MAZE, player))
    print("你赢了！")


if __name__ == "__main__":
    main()
