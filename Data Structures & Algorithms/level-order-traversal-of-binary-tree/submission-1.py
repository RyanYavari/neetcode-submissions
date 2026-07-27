# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        '''

        track level of each node when doing dfs
        if level doesnt exist, create new list for the level 


        '''

        output = []

        def dfs(root, level):
            if not root:
                return None
            if len(output) == level:
                output.append([])
            
            output[level].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)

        
        dfs(root, 0)

        return output





        