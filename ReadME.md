# Report of my DFS AND BFS implementation

## Introduction
The objective of this project was to implement and compare the performance of two well-known pathfinding algorithms, DFS and BFS, in solving a maze. The maze, depicted in Figure 1, serves as the testing ground for these algorithms. The "8" represents the starting point, the "9" represents the goal, "1" denotes accessible paths, and "0" indicates roadblocks.

![image](https://github.com/MorrisSimons/SCH_Applied_ai_assignment_1/assets/38280463/06ad1eef-711c-4764-9e48-849ebc77425f)



## TASK 1 Manual Implementation

### BFS
In the BFS approach, the algorithm was allowed to explore the maze much like the flow of water, seeking the fastest path to the goal. The exploration process adhered to a breadth-first strategy.

### DFS
For the DFS implementation, a right-first rule was adopted, meaning the algorithm would prioritize moving right, then up, left, and finally down. This approach aimed to explore deeper into the maze before backtracking.

### Conclusion
In the context of this manual maze-solving scenario, it was observed that the Depth-First Search (DFS) algorithm exhibited superior performance compared to the Breadth-First Search (BFS) algorithm. However, it is essential to recognize that this outcome is not universally applicable; DFS may outperform BFS in specific instances but is susceptible to losing its way when venturing too deeply into the maze. In contrast, BFS methodically explores multiple pathways.

Furthermore, it is worth noting that these algorithms come with distinct memory requirements. DFS tends to consume less memory, while BFS demands more extensive memory utilization due to its breadth-first nature.

To simplify the selection between DFS and BFS, it can be summarized as follows: BFS is particularly effective when the target is nearby, as it systematically explores all potential paths. On the other hand, DFS shines when the target is distant, prioritizing speed over memory efficiency in situations where ample memory resources are available.

![ai uppgift 1](https://github.com/MorrisSimons/SCH_Applied_ai_assignment_1/assets/38280463/67b69dd1-99ed-43f8-a767-74a5a4a78cab)


## Task 2 Implementation Details

### DFS (Depth-First Search)
Initially, a menu structure was developed to facilitate interaction with the algorithm. The DFS algorithm was chosen as the starting point due to its perceived simplicity. Object-oriented programming (OP) principles were applied to structure the code. Multiple iterations were required to refine the implementation, with inspiration drawn from external sources such as  [scoure Huseyin gave](https://www.educative.io/answers/what-is-the-maze-problem). 

### BFS (Breadth-First Search)
Following the completion of the DFS implementation, work on the BFS algorithm commenced. The familiarity gained from working with DFS expedited the development of the BFS solution. Similar conditions for movement, cell traversal, and path tracking were employed. Instead of utilizing a stack, as done in DFS, a queue-based approach was used in BFS. Several iterations were undertaken to rectify mirroring issues, ultimately leading to the successful generation of desired mazes.

![Untitled](https://github.com/MorrisSimons/SCH_Applied_ai_assignment_1/assets/38280463/242d5854-ffd5-4209-87e5-bab0eaa96be0)


### Conclusion 
In conclusion, this project demonstrated the successful implementation of DFS and BFS algorithms for maze solving. The code was designed to be concise and efficient, but there remain opportunities for further enhancement. Future improvements include:

Refactoring the code by creating new classes for the save_output_json and apply_path_to_maze functions to enhance code organization.
Implementation of pylint for code quality assessment.
Addition of comprehensive comments for code documentation and readability.
These enhancements aim to make the code more robust, maintainable, and comprehensible, thus facilitating future development and research in this domain.
