# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        '''

        root = preorder[0] 

        - length of left subtree = len(inorder[0: index of root.val]
        - recursively build the left subtree from preorder[index of root.val: index + lengthLeftTree)
        - root of left tree = preorder[1:mid+1]
        -  length of right subtree = len(inorder[index of root.val: end]
        - recursively build the right subtree from preorder[index + lengthLeftTree: end)
        - root of right tree = preorder[mid+1:]


        '''

        if not preorder or not inorder:
            return None

        
        root = TreeNode(preorder[0])  #first element in preorder is always the root
        mid = inorder.index(preorder[0]) # find root in inorder

        inorderLeft = inorder[:mid] # everything before root's index is the left subtree (inorder visits left, root, right)
        inorderRight = inorder[mid+1:] # everything after root's index is the right subtree

        preorderLeft = preorder[1:mid+1] #grabs the left subtree's preorder (starts right after root at index 1, and has mid elements, so it ends at index mid+1 exclusive)
        preorderRight = preorder[mid+1:] # grabs everything after that, which must be the right subtree's preorder




        root.left = self.buildTree(preorderLeft, inorderLeft) 

        root.right = self.buildTree(preorderRight, inorderRight)
        

        return root

     


        
            









        