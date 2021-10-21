# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, t = head, 1
        while curr.next:
            curr = curr.next
            t += 1

        if t == n:
            return head.next

        k = t - n
        curr, i = head, 1
        while i < k:
            curr = curr.next
            i += 1

        if k == 0:
            curr.next = None
        else:
            curr.next = curr.next.next

        return head
