# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):

        def sameTree(p,q):
            if not p and not q:
                return True
            if not p and q:
                return False
            if not q and p:
                return False
            if p.val != q.val:
                return False
            return sameTree(p.left,q.left) and sameTree(p.right,q.right)
  
        def dfs(root,subroot):
            if root is None:
                return False
            if subroot is None:
                return False
            if root.val == subroot.val:
                if sameTree(root,subroot):
                    return True
            return dfs(root.left,subroot) or dfs(root.right,subroot)
        
        return dfs(root,subRoot)