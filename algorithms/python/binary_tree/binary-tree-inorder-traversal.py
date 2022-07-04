# https://leetcode.com/problems/binary-tree-inorder-traversal

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderRecursive(self, root: TreeNode, arr: List[int]) -> None:
        if root:
            self.inorderRecursive(root.left, arr)
            arr.append(root.val)
            self.inorderRecursive(root.right, arr)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []
        self.inorderRecursive(root, arr)
        return arr
