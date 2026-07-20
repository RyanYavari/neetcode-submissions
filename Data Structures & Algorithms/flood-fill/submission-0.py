class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


        '''
        Matrix DFS

        ROWS, COLS = len(image), len(image[0])

        5 base cases

        add to visited hashSet

        perform 4 direction search and update values

        remove from visited hashSet

        return image



        '''
        orig = image[sr][sc]

        if orig == color:
            return image

        ROWS, COLS = len(image), len(image[0])
        


        def dfs(r, c):

            # if passes base cases, then color
            if min(r, c) < 0 or r >= ROWS or c >= COLS or image[r][c] != orig:
                return        
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        dfs(sr, sc)
        return image