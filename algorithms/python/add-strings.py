# https://leetcode.com/problems/add-strings/description/
import math


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)
        res, c = '', 0
        for i in range(max_len - 1, -1, -1):
            a = int(num1[i]) + int(num2[i]) + c
            c = math.floor(a / 10)
            if i != 0:
                res = str(a % 10) + res
            else:
                res = str(a) + res

        return res
