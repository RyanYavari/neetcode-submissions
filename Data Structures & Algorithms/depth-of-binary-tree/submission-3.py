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
        
        depthRight = self.maxDepth(root.right)
        depthLeft = self.maxDepth(root.left)
        
        return 1+max(depthRight, depthLeft)
        


        