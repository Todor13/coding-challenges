# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _sortedListToBST(self, sorted_list: list) -> Optional[TreeNode]:
        if not sorted_list:
            return None
        root = len(sorted_list) // 2
        return TreeNode(sorted_list[root], self._sortedListToBST(sorted_list[:root]),
                        self._sortedListToBST(sorted_list[root + 1:]))

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        sorted_list = []
        while head:
            sorted_list.append(head.val)
            head = head.next

        return self._sortedListToBST(sorted_list)
