class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        '''
        edge cases:
        no treasure chest -> assume always treasure chest
        1 < n,m < 100
            On^2 is valid 


            Input: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

        Level by level traversal from multiple cells at once -> Multi source BFS 

        On^2 complexity 

        Strat:

        1. find our treasure chests
            add to queue and visit set
        2. perform bfs from treasure chests
            pop curr cell from queue
            base case check
                is this land?
            
            if land:
                change value of land to curr distance in our bfs loop (represents distance from treasure chest)
        
        return grid


        Input: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

queue =  ())
0
visit = {(0, 2), (3, 0), (0,3), (1,2), (2,0), (1,1), (1,0), (3,2), (0,0)}
distance = 6

        '''

        #initialize variables
        queue = deque()
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [[1, 0], [0,1], [-1,0], [0,-1]]

        #initialize our treasure chests

   
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visit.add((r,c))
        
        distance = 1
        while(queue):
            for i in range(len(queue)):
                # dequeue current cell
                r, c = queue.popleft()

                #search neighbors (up, down, left, right)
                
                for dr, dc in neighbors:
                    nr, nc = dr+r, dc+c

                    #check base case to see if current cell is land
                    if (min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit or grid[nr][nc] != 2147483647):
                        continue

                    #current cell is land. replace cell value with distance from nearest treasure chest
                    grid[nr][nc] = distance
                    visit.add((nr, nc))
                    queue.append((nr,nc))
            distance += 1
  

