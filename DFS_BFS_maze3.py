import json
from collections import deque



class DFS:
    def __init__(self, maze):
        self.maze = maze
        self.visited = set()
        self.path = []

    def find_path(self, start, end):
        def dfs_helper(node):
            #Check if the current position is the goal
            if node == end:
                self.path.append(node)
                return True
            self.visited.add(node)
            #Define possible moves up, down, left, right
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            #Try each possible move
            for move in moves:
                next_node = (node[0] + move[0], node[1] + move[1])
                if (
                    0 <= next_node[0] < len(self.maze)
                    and 0 <= next_node[1] < len(self.maze[0])
                    and self.maze[next_node[0]][next_node[1]] == 1
                    and next_node not in self.visited
                ):
                    if dfs_helper(next_node):
                        self.path.append(node)
                        return True
            return False
        if dfs_helper(start):
            self.path.reverse()  #Reverse the path to get it from start to end

class BFS:
    def __init__(self, maze):
        self.maze = maze
        self.visited = set()
        self.path = []

    def find_path(self, start, end):
        queue = deque()
        queue.append(start)
        visited = set()
        #Define possible moves up, down, left, right
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            current_node = queue.popleft()
            #print(current_node)
            self.path.append((current_node[1],current_node[0]))
            if current_node == end:
                break
            for move in moves:
                next_node = (current_node[0] + move[0], current_node[1] + move[1])
                if (
                    0 <= next_node[0] < len(self.maze)
                    and 0 <= next_node[1] < len(self.maze[0])
                    and self.maze[next_node[1]][next_node[0]] == 1
                    and next_node not in visited
                ):
                    queue.append(next_node)
                    visited.add(next_node)
        if current_node == end:
            return True
        else:
            self.path = []

def save_output_json(maze_output_file_name, maze):
    with open(maze_output_file_name, "w") as maze_output_file:
        json.dump(maze, maze_output_file)
    

def apply_path_to_maze(maze,path):
    new_path = []
    #Create the new maze
    for i in range(len(maze)):
        new_path.append([])
        for j in range(len(maze[i])):
            new_path[i].append(0)
    #Apply the path to the new maze
    for node in path:
        new_path[node[0]][node[1]] = 1
    return new_path

def main():
    #Load the maze
    try:
        with open("input.json", "r") as maze_input_file:
            maze = json.load(maze_input_file)
    except:
        print("Error: input.json not found")
        return
    #Find start and end values
    start, end = None, None
    for index, row in enumerate(maze):
        for index2, col in enumerate(row):
            if col == 8:
                start = (index, index2)
                maze[index][index2] = 1
            elif col == 9:
                end = (index, index2)
                maze[index][index2] = 1
    if start == None or end == None:
        print("Error: start or end not found")
        return    

    #Ask which algorithm to use
    print("what algoritm do you want to use?")
    print("1. DFS")
    print("2. BFS")
    print("choose by entering 1 or 2")
    choice = 0
    while choice != 1 and choice != 2:
        try:
            print("=====================================")
            choice = int(input("Enter your choice: "))
            print("=====================================")
        except ValueError:
            print("ValueError: Please enter a number")
        if choice == 1:
            print("Running DFS on this maze")
            for i in maze:
                print(i)
            print("============")
            dfs = DFS(maze)
            dfs.find_path(start, end)
            if dfs.path == []:
                print("No path found")
                return
            path = apply_path_to_maze(maze, dfs.path)
            save_output_json("output.json", path)
        elif choice == 2:
            print("Running BFS on this maze")
            for i in maze:
                print(i)
            print("============")
            bfs = BFS(maze)
            bfs.find_path(start, end)
            if bfs.path == []:
                print("No path found")
                return
            path = apply_path_to_maze(maze, bfs.path)
            save_output_json("output.json", path)
        else:
            print("Please enter a valid choice")
            continue
        break
    
    #Display the path
    try:
        choice = input("[y/n] to display output: ")
        if choice == "Y" or choice == "y":
            for i in path:
                print(i)
        else:
            pass
    except:
        print("Error")

    #Ask to run again
    try:
        choice = input("[y/n] to run again: ")
        if choice == "Y" or choice == "y":
            main()
        else:
            print("Exiting")
            return
    except:
        print("Error")

if __name__ == "__main__":
    main()
    
