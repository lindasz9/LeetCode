# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Helper function to move to the next node based on the target value
        # Returns (next_node, direction): 0 = left, 1 = right, 2 = found
        def nxt(node, i):
            if not node:
                pass
            if i > node.val:
                return (node.right, 1)
            elif i < node.val:
                return (node.left, 0)
            return (node, 2)

        pnode, qnode = root, root  # Start traversal for both p and q from root
        plast, qlast = 0, 0        # Direction trackers for both nodes

        while True:
            now = pnode           # Current node where both traversals meet
            pnode, plast = nxt(pnode, p.val)  # Move p traversal
            qnode, qlast = nxt(qnode, q.val)  # Move q traversal

            # If p and q go in different directions, current node is LCA
            if plast != qlast:
                return now
