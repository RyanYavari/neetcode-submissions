# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        '''
        lookng for depth -> DFS

        find the height of the tree by finding the height of its root


        '''

        if not root:
            return 0
        
        depthRight = 1 + self.maxDepth(root.right)
        depthLeft = 1 + self.maxDepth(root.left)
        
        return max(depthRight, depthLeft)
        


        