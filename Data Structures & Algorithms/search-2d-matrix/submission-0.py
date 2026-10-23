class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        '''
        loop through each row in matrix
            for every row, perform binary search #allowed because rows are sorted in non decreasing order
                return true if target is found
        
        return false


        '''


        for r in range(len(matrix)):

            #binary search
            lo, hi = 0, len(matrix[r]) - 1

            while lo <= hi:
                mid = (lo+hi)//2

                if matrix[r][mid] == target:
                    return True
                elif matrix[r][mid] < target: #smaller than target, increase lo
                    lo = mid+1
                elif matrix[r][mid] > target: #bigger than target, shrink hi
                    hi = mid-1
            
        
        return False

        