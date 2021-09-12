# https://leetcode.com/problems/isomorphic-strings


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping, used = dict(), set()
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in used:
                    mapping[s[i]] = t[i]
                    used.add(t[i])
                else:
                    return False

        return True
