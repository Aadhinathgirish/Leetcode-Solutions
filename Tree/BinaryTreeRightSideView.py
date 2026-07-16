# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        queue = [root]
        res = []
        ans = [root]
        while queue:
            Qlen = len(queue)
            output = ans[-1]
            res.append(output.val)
            ans = []
            for i in range(Qlen):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                    ans.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                    ans.append(cur.right)
        return res
           
                
        