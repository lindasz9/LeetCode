# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None  # Base case: empty node returns None
        
        # Recursively invert right and left subtrees and swap them
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root  # Return the root of the inverted subtree
