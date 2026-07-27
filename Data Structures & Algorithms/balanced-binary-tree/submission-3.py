# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        '''

        DFS

        find height of left subtree and right subtree. if height difference is less than 2, tree is balanced. 

        O(n) approach with dfs:
        
        dfs(node):
            if not root: #root is a leaf, return true and height of 0

            #if its node, find right and left subtree height to see if tree is balanced

                if either left or right subtree is not balanced (false) OR  their height difference is mroe than one, return false. else return true
        

        '''

        #DFS

        def dfs(root):
            #if root is Null -> Tree is balanced and has a height of 0
            if not root:
                return [True, 0]
            
            # if root exists, determine if its balanced by searching its right and left child.

            right = dfs(root.right)
            left = dfs(root.left)

            rightHeight = right[1]
            leftHeight = left[1]

            # check if balanced

            balanced = right[0] and left[0] and abs(rightHeight - leftHeight) <= 1

            #calculate height. 
            height = 1 + max(leftHeight, rightHeight)

            return [balanced, height]
        

        return dfs(root)[0]
            


         


            

            




        



        



