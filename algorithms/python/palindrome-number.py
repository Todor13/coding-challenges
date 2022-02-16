# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        curr = x
        rev = 0
        while curr > 0:
            rev = rev * 10 + curr % 10
            curr //= 10

        return rev == x
