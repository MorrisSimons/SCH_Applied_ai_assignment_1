import json

def BFS():
    print("BFS")
    return


class DFS:
    def __init__(self,maze, path) -> None:
        self.maze = maze
        self.path = path
        self.queue = []
        self.visited = []

    def set_path(self, new_path):
        self.path = new_path
        return new_path

    def _SUB_DFS_(self, col, row):
        maze = self.maze
        for i in self.path:
            print(i)
        input("Press Enter to continue...")
        
        if col+1 <= len(maze[0]) and row+1 <= len(maze):
            print(f"col+1:{col+1} <= len({len(maze[0])} row +1: {row+1} <= len({len(maze)}))" )
            if maze[row][col+1] == 1:
                # Fix me - set path
                self.path[row][col+1] = 1
                print(f"setting this path 1")
                print(f"row: {row} col: {col}")
                self._SUB_DFS_(col+1, row)
            # check if up is a wall
            elif maze[row-1][col] == 1 and row-1 >= 0:
                # Fix me - set path
                self.path[row-1][col] = 1
                print(f"setting this path 2")
                print(f"row: {row} col: {col}")
                self._SUB_DFS_(col, row-1)
            # check if down is a 
            elif maze[row+1][col] == 1 and row+1 > len(maze):            
                # Fix me - set path
                self.path[row+1][col] = 1
                print(f"setting this path 3")
                print(f"row: {row} col: {col}")
                self._SUB_DFS_(col, row+1)
            # check if left is a wall
            elif maze[row][col-1] == 1 and col-1 >= 0:         
                # Fix me - set path
                self.path[row][col-1] = 1
                print(f"setting this path 4")
                print(f"row: {row} col: {col}")
                self._SUB_DFS_(col-1, row)
            else:
                print("reached end of maze")
                return
        else:
            print("dafuq")
            return
    def DFS_main(self,):
        print("Running Main")
        # open the maze file
        
        for row, items in enumerate(self.maze):
            for col, item in enumerate(items):
                if item == 1:
                    # check if right is a wall
                    print(col, row)
                    self.path[row][col] = 1
                    self._SUB_DFS_(col, row)
            #print(self.queue)
            for i in self.path:
                print(i)
        return

def DFS_setup():
    print("Running DFS setup")
    path = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
        ]
    # file navigation
    maze_file_name = "input.json"
    maze_output_file_name = "output.json"
    with open(maze_file_name, "r") as maze_file:
        maze = json.load(maze_file)
        for i in maze:
            print(i)
    DFS_OBJ = DFS(maze, path)
    DFS_OBJ.DFS_main()
    return

def main():
    print("what algoritm do you want to use?")
    print("1. DFS")
    print("2. BFS")
    print("choose by entering 1 or 2")
    Choice = 0
    while Choice != 1 or Choice != 2:
        try:
            print("=====================================")
            Choice = int(input("Enter your choice: "))
            print("=====================================")
        except ValueError:
            print("ValueError: Please enter a number")
        if Choice == 1:
            DFS_setup()
        elif Choice == 2:
            BFS()
        else:
            print("Please enter a valid choice")
            continue
        break
if __name__ == "__main__":
    DFS_setup()
