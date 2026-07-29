# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        '''

        good node X = path from root -> X where no node is > X.val

        recursive comparison -> DFS

        def dfs(root):
            if not root: 
                return True
            
            if root.left or root.right < root.val for the entire path from the root to null, then it's a valid path
                return False
            
            # at this point, all the dfs values were greater, so increment count by 1

            return True

        count = 0

        if not root:
            return 0
        
        dfs(root)
        return count


        '''

        # if current node's value is greater than or equal to maxVal, continue searching
        # if not, stop dfs
        def dfs(root, maxVal):
            nonlocal count
            if not root:
                return 
            

            if root.val >= maxVal:
                count += 1
                maxVal = root.val
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        count = 0
        if not root:
            return 0
        
        dfs(root, root.val)
        
        return count
    
    







        