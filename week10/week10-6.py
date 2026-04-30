#week10-6.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helper(root):
            if root == None: return 0, 0

            Lans1, Lans2 = helper(root.left)
            Rans1, Rans2 = helper(root.right)
            self.ans = max(self.ans, Lans2+1, Rans1+1)
            return Lans2 + 1, Rans1 + 1
        helper(root)
        return self.ans - 1
