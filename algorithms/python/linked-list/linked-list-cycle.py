# https://leetcode.com/problems/linked-list-cycle

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
            if fast == slow:
                return True
        return False
