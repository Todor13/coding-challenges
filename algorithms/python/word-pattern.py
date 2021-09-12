# https://leetcode.com/problems/word-pattern


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(s) != len(pattern):
            return False

        mapping, used = dict(), set()
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != pattern[i]:
                    return False
            else:
                if pattern[i] not in used:
                    mapping[s[i]] = pattern[i]
                    used.add(pattern[i])
                else:
                    return False

        return True
