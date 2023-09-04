import json



def DFS_RECURSIVE(maze, path, col, row):
    #Check if the current position is the goal
    if maze[row][col] == 9:
        return True

    #Mark the current position as visited
    path[row][col] = 8

    #Define possible moves (up, down, left, right)
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    #Try each possible move
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        
        #Check if the new position is valid
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
            #Recursively explore the new position
            if DFS_RECURSIVE(maze, path, new_col, new_row):
                return True
    
    #If no valid move leads to the goal, backtrack
    path[row][col] = 0
    return False
    


def DFS():
    print("starting DFS Function")
    #Settings for DFS
    maze_file_name = "input.json"
    maze_output_file_name = "output.json"
    start_index = []
    end_index = []
    #Open the maze file
    with open(maze_file_name, "r") as maze_file:
        print("============")
        print("this is your maze")
        maze = json.load(maze_file)
        for i in maze:
            print(i)
        print("============")
    #Find the start and end of the maze
    for row, items in enumerate(maze):
        for col, item in enumerate(items):
            if item == 8:
                start_index.append(row)
                start_index.append(col)
            elif item == 9:
                end_index.append(row)
                end_index.append(col)
        if len(start_index) == 2 and len(end_index) == 2:
            break
    #Create the path array
    path = []
    for i in range(len(maze)):
        path.append([])
        for j in range(len(maze[i])):
            path[i].append(0)
    #Create the DFS function
    if DFS_RECURSIVE(maze, path, start_index[1], start_index[0]):
        print("Path found!")
        for i in path:
            print(i)
        save_output_json(maze_output_file_name, maze)
    else:
        print("No path found.")
    
def BFS():
    pass

def save_output_json(maze_output_file_name, maze):
    with open(maze_output_file_name, "w") as maze_output_file:
        json.dump(maze, maze_output_file)


def main():
    print("what algoritm do you want to use?")
    print("1. DFS")
    print("2. BFS")
    print("choose by entering 1 or 2")
    Choice = 0
    while Choice != 1 and Choice != 2:
        try:
            print("=====================================")
            Choice = int(input("Enter your choice: "))
            print("=====================================")
        except ValueError:
            print("ValueError: Please enter a number")
        if Choice == 1:
            DFS()
        elif Choice == 2:
            BFS()
        else:
            print("Please enter a valid choice")
            continue
        break
if __name__ == "__main__":
    DFS()
