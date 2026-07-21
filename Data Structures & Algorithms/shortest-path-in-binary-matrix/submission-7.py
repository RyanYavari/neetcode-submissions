class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:


        '''

        output: length of shortest clear path, if no clear path return -1

        shortest path -> BFS 

        clear path: path from top left (0,0) to bottom right (n-1, n-1)
            all cells are 0
            all adjacent cells are 8-directionally connected (edge or corner)
        
        8-directionally neighbors = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1, -1], [-1, 1], [1, 1]]

        strat:


        intialize (0,0)
            add to visit set and queue


        length = 0 # min number of layers
        bfs
            increment length atthe end of each layer

        return length 

        '''

        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        # initialize (0,0), and check if cell is valid. if not, return -1
        if grid[0][0] == 1:
            return -1
        
        visit.add((0,0))
        queue.append((0,0))

        # bfs

        length = 1
        while(queue):
            for i in range(len(queue)):
                #popleft queue
                r, c = queue.popleft()

                # check if cell is at target
                    # return length
                if r == ROWS-1 and c == COLS-1:
                    return length

                # bfs on neighbors
                neighbors = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1, -1], [-1, 1], [1, 1]]
                for dr, dc in neighbors:
                    # check base cases
                    if (min(dr+r, dc+c) < 0 
                    or dr+r == ROWS or dc+c == COLS 
                    or (dr+r,dc+c) in visit 
                    or grid[dr+r][dc+c] == 1):
                        continue
                   # add to visit set and queue
                    queue.append((dr+r, dc+c))
                    visit.add((dr+r, dc+c))
            length += 1
        
        
        return -1









        