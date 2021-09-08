# https://leetcode.com/problems/rotate-list

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None:
            return head

        n = 0
        curr = head
        tail = None
        while curr:
            tail = curr
            curr = curr.next
            n += 1

        if k % n == 0:
            return head

        idx = n - (k % n)
        prev = None
        curr = head
        for i in range(idx):
            prev = curr
            curr = curr.next

        prev.next = None
        tail.next = head
        return curr
