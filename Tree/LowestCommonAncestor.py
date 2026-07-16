# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return 0
        if (p.val< root.val and q.val > root.val)or (p.val > root.val and q.val < root.val):
            return root
        if p.val == root.val and (q.val> p.val or q.val<p.val):
            return p
        if q.val == root.val and (p.val < q.val or p.val > q.val):
            return q
        if p.val < root.val and q.val< root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        