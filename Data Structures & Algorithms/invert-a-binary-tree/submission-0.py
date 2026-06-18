# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        '''

        # inverting a binary tree -> swapping every node's left and sub tree
        
        check if root exists, if not return null

        swap left and right child

        DFS on left and right child

        return root


        '''

        if not root:
            return None
        
        #swap left and right child
        node = root.left
        root.left = root.right
        root.right = node

        #perform DFS on children
        self.invertTree(root.left)
        self.invertTree(root.right)


        return root

        


        