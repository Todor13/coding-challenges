"""
https://leetcode.com/problems/count-servers-that-communicate/description/

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server.
Two servers are said to communicate if they are on the same row or on the same column.


Return the number of servers that communicate with any other server.

Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.


Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m <= 250
    1 <= n <= 250
    grid[i][j] == 0 or 1

"""

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        idx = 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    grid[r][c] = idx
                    idx += 1

        s = set()
        for r in range(len(grid)):
            res = [x for x in grid[r] if x != 0]
            s.update(res if len(res) > 1 else [])

        for row in list(map(list, zip(*grid))):
            res = [x for x in row if x != 0]
            s.update(res if len(res) > 1 else [])

        return len(s)


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    print(sol.countServers(grid))
