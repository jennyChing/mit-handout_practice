# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: # root == None, go thourgh till the end without finding non-valid nodes in BST
            return True
        if root.val <= floor or root.val >= ceiling: # non-valid nodes
            return False
        # recursively check left and right nodes of root
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling) # only True and True will return that the BST is valid (great logic!)


