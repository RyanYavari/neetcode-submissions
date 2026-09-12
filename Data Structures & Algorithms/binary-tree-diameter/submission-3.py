# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        '''

        Looking for longest length -> DFS

        max diameter of any tree = leftHeight + rightHeight

        height of a tree = 1 + max(leftHeight, rightHeight)

        1. initialize diameter = 0

        2. dfs
            for every dfs run, update diameter with max(diameter, node's diameter)
        
        return diameter


        
        
        
        '''

        diameter = 0

        def dfs(root):
            nonlocal diameter

            if not root:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            diameter = max(diameter, leftHeight + rightHeight)
            
            return 1+max(leftHeight, rightHeight)
        
        dfs(root)

        return diameter



