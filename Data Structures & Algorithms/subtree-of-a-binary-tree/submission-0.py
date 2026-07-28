# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        '''

        dfs -> recursively run through a subtree -> return a value for that run
        also more comfortable with dfs for this scenario


        1. traverse through root note until we find subroot node

        traverse through tree with dfs
            if root == subroot
                perform dfs
                    if it returns true, return True
                if False, keep traversing through tree
        
        if you traversed through the entire tree and didnt return True -> no subtree exists in tree -> return False 

        2. perform dfs/bfs on subroot to return True or False on whether it matches subRoot
        

        Time complexity -> traversing through every node -> O(n) w dfs
        Space -> O(n) -> max size of the queue and visit sets



        Input: root = [1,2,3,4,5], subRoot = [2,4,5]

        curr root = 2
        curr subRoot = 2   


        isSubtree(2, 2) -> True -> True -> True -> True
                                     -> True -> True -> True

        '''

        #traverse through tree until you find root == subroot

        if not root and not subRoot:
            return True

        if not root:
            return False


        # dfs function
        def dfs (node, sub):

            #node and subroot are both false -> same -> true
            if not node and not sub:
                return True
            #only one of the nodes are false -> not same -> false
            if not node or not sub: 
                return False
            
            # if node values are same -> potentially same tree -> search children.
                # if they both lead to (ndoe and subroot are both false) then it means all values are equal -> same tree -> recursively returns True
            if node.val == sub.val:
                return dfs(node.left, sub.left) and dfs(node.right, sub.right)
            
            #if node values arent the same -> not same subtree -> return False
            return False 
        
        # traverse through root

        #if root == subRoot, check if same tree
        if root.val == subRoot.val:
            if dfs(root, subRoot): #if there is at least one valid subtree in root -> return True
                return True
        
        #if not equal, continue searching root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        #if you searched the entire root and didnt find subRoot, return False
        return False











        













        