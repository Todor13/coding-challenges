# https://leetcode.com/problems/binary-tree-preorder-traversal

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderRecursive(self, root: TreeNode, arr: List[int]) -> None:
        if root:
            arr.append(root.val)
            self.preorderRecursive(root.left, arr)
            self.preorderRecursive(root.right, arr)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.preorderRecursive(root, arr)
        return arr
