# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        '''

        need to know the ancestor chain -> DFS

        whever split occurs (search left and right) OR if root == p or root = q:
            we found the lowest common ancestor

        if p.val and q.val < root.val
            search left subtree
        if p.val and q.val > root.val
            search right subtree


        
        if split occurs -> lowest common ancestor



        '''

        if not p or not q or not root:
            return None
        
        if q.val < root.val and p.val < root.val: #both q and p and lower than root, search left
            return self.lowestCommonAncestor(root.left, p, q)
        elif q.val > root.val and p.val > root.val: #both q and p and larger than root, search right
            return self.lowestCommonAncestor(root.right, p, q)
        else: #q or p == root OR a split occurs -> both indicate that this is the LCA (lowest common ancestor)
            return root
        




        
        