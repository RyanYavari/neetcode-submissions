# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        '''

        level by level traversal, only appending the right most node
            right most node = last node in queue 

        level by level traversal -> BFS

        add queue[-1] to the output. this retrieves the last element in the queue which is the right most node


        '''
        #initialize queue with root
        queue = deque()
        output = []


       
        if root:
            queue.append(root)
        
        #bfs

        while(queue):
            output.append(queue[-1].val)
            for i in range(len(queue)):
                
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
        
        return output


        

        