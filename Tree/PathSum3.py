# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root,targetSum):   
        count = 0
        hashmap = {0:1}
        def dfs(root,curSum):
            nonlocal count
            if not root:
                return None
            curSum +=  root.val
            if (curSum-targetSum) in hashmap:
                count += hashmap[curSum-targetSum]
            hashmap[curSum] = 1 + hashmap.get(curSum,0)
            dfs(root.left,curSum)
            dfs(root.right,curSum)
            hashmap[curSum]-=1
            return 
        dfs(root,0)
        return count

