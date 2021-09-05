# https://leetcode.com/problems/group-anagrams

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in range(len(strs)):
            key = "".join(sorted(strs[s]))
            d[key].append(strs[s])
        return [d[x] for x in d.keys()]
