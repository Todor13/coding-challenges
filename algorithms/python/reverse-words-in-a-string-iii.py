# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseString(self, s: str) -> str:
        s = [char for char in s]
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return ''.join(s)

    def reverseWords(self, s: str) -> str:
        rev = []
        for w in s.split():
            rev.append(self.reverseString(w))
        return ' '.join(rev)
