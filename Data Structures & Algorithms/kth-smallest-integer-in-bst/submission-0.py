# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        '''

        return kth smallest value from a BST


        In order traversal on BST -> DFS

        arr = []

        in order traversal DFS to populate arr

        return arr[len(arr)-k]
        '''

        arr = []

        def inorder(node):

            if not node:
                return None
            
            inorder(node.left)

            arr.append(node.val)

            inorder(node.right)
        

        inorder(root)

        return arr[k-1]
