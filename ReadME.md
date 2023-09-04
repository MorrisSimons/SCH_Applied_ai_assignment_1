# Report of my DFS AND BFS implementation

## Quick guide
- 8 starting value
- 9 goal value
- 1 is avalibel path
- 0 is road block
- Add an maze that looks like this
  
![image](https://github.com/MorrisSimons/SCH_Applied_ai_assignment_1/assets/38280463/09718d6d-8a28-460c-b749-ae97cb76d388)



## TASK 1

This is my result from the first task when we worked manually. It went good done some BFS and DFS before so it went fast. The only hard thing was that it doesn't look that good when you write for hand without support lines to keep you in check. Small introduction to how i solved it

For the BFS i let it flow like water to find the fastest path to the goal.

For the DFS i went with the right rule, not sure witch way you are suposed to go as the standard way but i choose to go right, up, left and down
![image](https://github.com/MorrisSimons/SCH_Applied_ai_assignment_1/assets/38280463/01cff01a-98d3-4a97-a439-50b08d10938a)


## Task 2

### DFS
i started with an menu then i started to work with DFS because i thought that would be easiest way to go. I used OP to structure up everything nice took awhile to get used to it again so i tried 2 times before it got abit to messy and on the 3:d time i managed to solve when i took some inspiration from the [scoure Huseyin gave](https://www.educative.io/answers/what-is-the-maze-problem). 

### BFS
After this i started to work on BFS this went faster due to me useing simliar methods with the move conditions, moves and instead of useing a stack like i did in DFS i used an BFS. I had some mirroing bugs 1 had 1 more senario that i forgot to photo graph but senario 1 and 2 are wrong while senario 3 is the correct on. Took a while to figure out what combinations was right to get the maze i wanted.
![Untitled](https://github.com/MorrisSimons/SCH_Applied_ai_assignment_1/assets/38280463/2ccebcb2-0509-493e-b66b-b4644cf93ad9)

### Conclusion 
I managed to keep the code farily short and effective. It has some more approvments you can do in the main menu sections with error handeling where you can add the N/n senarios and else senarios. Other areas of improvements are
- add the save_output_json and apply_path_to_maze function to an new class to structure up the code a bit more
- use pylint.
- Add some more comments.
