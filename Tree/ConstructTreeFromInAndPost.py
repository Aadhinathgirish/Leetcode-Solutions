# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        hashmap = {}
        for i, val in enumerate(inorder):
            hashmap[val] = i

        def build(postStart, postEnd, inStart, inEnd):
            if postStart > postEnd:
                return None

            rootVal = postorder[postEnd]
            root = TreeNode(rootVal)

            index = hashmap[rootVal]
            leftSize = index - inStart

            root.left = build(
                postStart,
                postStart + leftSize - 1,
                inStart,
                index - 1
            )

            root.right = build(
                postStart + leftSize,
                postEnd - 1,
                index + 1,
                inEnd
            )

            return root

        return build(0, len(postorder) - 1, 0, len(inorder) - 1)