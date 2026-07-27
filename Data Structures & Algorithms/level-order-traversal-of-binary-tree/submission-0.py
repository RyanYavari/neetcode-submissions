# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''

        do bfs
            before the for loop create a list
            during the loop, add the items to the list
            after each completed for loop for the queue, append list to output list


        '''

        queue = deque()
        output = []


        if root:
            queue.append(root)
        
        
        while(queue):
            order = []
            for i in range(len(queue)):
                curr = queue.popleft()

                order.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            output.append(order)
        
        return output


        