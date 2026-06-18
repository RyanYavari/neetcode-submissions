# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        '''

        input: binary tree root node

        output: depth of tree

        is it sorted?  no
        
        0 < num of nodes < 100

        Breadth first search -> # of levels in tree

        return levels

        breadth first search algo:

        from collections import deque

        if not root:
            return 0
        
        if there is a root, we know depth is > 0

        queue = deque()

        depth = 0

        
        while queue > 0:
            levels += 1
            loop through items in queue:
                add children of items in queue to queue
            
        return levels

        '''

        queue = deque()

        if root:
            queue.append(root)
        
        depth = 0
        while len(queue) > 0:
            
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            depth += 1
        
        return depth












        