from random import shuffle
from random import randrange

PATH = " "
WALL = "#"

def fancy_print(arr):
    for row in arr:
        temp = ""
        for i in row:
            temp += str(i) + " "
        print(temp)

def all_visited(maze: [[int]]) -> bool:
    for row in maze:
        for cell in row:
            if not cell:
                return False
    return True


def build_maze(size: int) -> [[int]]:
    maze = []
    visited = []

    # fill maze with zeroes
    for i in range(size):
        row = []
        visited_row = []
        for j in range(size):
            row.append(WALL)
            visited_row.append(True)
        maze.append(row)
        visited.append(visited_row)

    # fill maze with unvisited cells
    for row in range(size):
        for col in range(size):
            if row % 2 == 1 and col % 2 == 1:
                maze[row][col] = PATH
                visited[row][col] = False
    digger_row = 1
    digger_flow = 1
    path = [(1, 1)]
    visited[1][1] = True

    while not all_visited(visited):
        directions = [0, 1, 2, 3]
        shuffle(directions)
        moved = False
        for d in range(4):
            direction = directions[d]
            if direction == 0 and digger_row - 2 > 0 and visited[digger_row - 2][digger_flow] == False:
                maze[digger_row - 1][digger_flow] = PATH
                digger_row -= 2
                path.append((digger_row, digger_flow))
                visited[digger_row][digger_flow] = True
                moved = True
                break

            elif direction == 1 and digger_flow + 2 < size and visited[digger_row][digger_flow + 2] == False:
                maze[digger_row][digger_flow + 1] = PATH
                digger_flow += 2
                path.append((digger_row, digger_flow))
                visited[digger_row][digger_flow] = True
                moved = True
                break

            elif direction == 2 and digger_row + 2 < size and visited[digger_row + 2][digger_flow] == False:
                maze[digger_row + 1][digger_flow] = PATH
                digger_row += 2
                path.append((digger_row, digger_flow))
                visited[digger_row][digger_flow] = True
                moved = True
                break

            elif direction == 3 and digger_flow - 2 > 0 and visited[digger_row][digger_flow - 2] == False:
                maze[digger_row][digger_flow - 1] = PATH
                digger_flow -= 2
                path.append((digger_row, digger_flow))
                visited[digger_row][digger_flow] = True
                moved = True
                break

        if path and not moved:
            digger_row, digger_flow = path.pop()

    while True:
        start = randrange(size)
        if maze[1][start] == PATH:
            maze[0][start] = PATH
            break
    while True:
        end = randrange(size)
        if maze[size - 2][end] == PATH:
            maze[size - 1][end] = PATH
            break

    return maze

fancy_print(build_maze(13))