# https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * max(n, 2)
        arr[0] = 1
        arr[1] = 2

        for i in range(2, n):
            arr[i] = arr[ i -1] + arr[ i -2]

        return arr[n - 1]
