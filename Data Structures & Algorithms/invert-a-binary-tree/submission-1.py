# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        '''

        if node is null, return None # ends recursive call

        swap left subtree with right subtree using a temp node

        recursively call left subtree
        recurisve call right subtreee


        '''

        if not root:
            return None
        
        tempNode = root.left
        root.left = root.right
        root.right = tempNode

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root