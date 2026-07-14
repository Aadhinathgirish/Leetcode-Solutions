# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            Qlen = len(queue)
            ans = []
            for i in range(Qlen):
                cur = queue.pop(0)
                ans.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(ans)
        return res
        