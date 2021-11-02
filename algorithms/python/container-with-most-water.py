# https://leetcode.com/problems/container-with-most-water

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        j, k = 0, len(height) - 1
        m_area = 0
        while j < k:
            diff = k - j
            m_area = max(m_area, diff * min(height[j], height[k]))
            if height[j] <= height[k]:
                j += 1
            else:
                k -= 1
        return m_area
