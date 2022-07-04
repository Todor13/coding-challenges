# https://leetcode.com/problems/range-sum-of-bst

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            if root.val < low:
                return self.rangeSumBST(root.right, low, high)

            if root.val > high:
                return self.rangeSumBST(root.left, low, high)

            sum = 0
            sum += self.rangeSumBST(root.left, low, high)
            sum += self.rangeSumBST(root.right, low, high)

            return root.val + sum
        return 0
