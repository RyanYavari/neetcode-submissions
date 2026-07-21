class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        '''

        8-directionally neighbors = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1, -1], [-1, 1], [1, 1]]


        shortest path -> bfs O(n^2)

        initialize first cell 

        bfs


        '''

        n = len(grid)
        visit = set()
        queue = deque()
        neighbors = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1, -1], [-1, 1], [1, 1]]

        #initialize first cell
        visit.add((0, 0)) 
        queue.append((0, 0, 1)) #row, col, length

        #bfs
            #loop through queue's snapshot length
            # popleft
            # check for edge cases
            # check if at target cell (last cell)
            # expand to neighbors
            # add to visit and queue


        while queue:
            #1) loop through queue
            for i in range(len(queue)):
                #2) popleft values
                r, c, length = queue.popleft()
                
                #3) edgecases check
                if (min(r,c) < 0 or
                r == n or c == n or
                grid[r][c] == 1):
                    continue
                
                #4) check if at target value
                if r == n-1 and c == n-1:
                    return length
                
                #5) expand to neighbors
                for dr, dc in neighbors:
                    if (r+dr, c+dc) not in visit:
                        # add to visit and queue
                        # increase length by 1 because we are expanding the path
                        visit.add((r+dr, c+dc))
                        queue.append((r+dr, c+dc, length+1))
        
        return -1
        

                


                

        






        