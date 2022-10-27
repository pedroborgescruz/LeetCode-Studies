"""
INVERT BINARY TREE
==================
Given the root of a binary tree, invert the tree, and return its root.
Pedro Cruz
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        # if we hit a null node, there's nothing to do
        if (root == None):
            return 
        
        # else swap roots of subtrees...
        root.left, root.right = root.right, root.left
        
        # and recursively do the same for their children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # finally, return my current root
        return root