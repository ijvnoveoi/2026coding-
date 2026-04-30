#week10-5.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = Counter()
        counter[0] = 1
        def helper(root, total):
            if root==None: return 0
            total += root.val
            counter[total] += 1
            ans = counter[total - targetSum]
            ans += helper(root.left, total)
            ans += helper(root.right, total)
            counter[total] -= 1
            return ans
        return helper(root, 0)
