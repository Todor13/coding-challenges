# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        next = None
        while curr:
            curr_next = curr.next
            curr.next = next
            next = curr
            curr = curr_next

        return next
