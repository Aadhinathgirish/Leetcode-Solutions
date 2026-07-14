# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        def dfs(root):
            if root is None:
                return 0
            total = 0
            if root.left and root.left.left is None and root.left.right is None:
                total+=root.left.val
            total += dfs(root.left)
            total += dfs(root.right)
            return total
        return dfs(root)
 