# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(root):
            if root is None:
                return 0
            leftheight = dfs(root.left)
            if leftheight == -1:
                return -1
            rightheight = dfs(root.right)
            if rightheight == -1:
                return -1
            if abs(leftheight-rightheight)>1:
                return -1
            return 1 + max(leftheight,rightheight)
        return dfs(root)!=-1
