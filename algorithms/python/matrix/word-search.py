"""
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.
"""

"""
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or idx >= len(word):
            return False
        if len(word) - 1 == idx and word[idx] == board[r][c]:
            return True
        elif len(word) - 1 == idx:
            return False

        if word[idx] == board[r][c]:
"""


class Solution:
    def exists_rec(self, board, r, c, word, idx, visited):
        if visited[r][c]:
            return False
        if idx == len(word) - 1:
            return True

        visited[r][c] = True
        result = []
        if r - 1 >= 0 and board[r - 1][c] == word[idx + 1]:
            result.append(self.exists_rec(board, r - 1, c, word, idx + 1, visited))
        if r + 1 < len(board) and board[r + 1][c] == word[idx + 1]:
            result.append(self.exists_rec(board, r + 1, c, word, idx + 1, visited))
        if c - 1 >= 0 and board[r][c - 1] == word[idx + 1]:
            result.append(self.exists_rec(board, r, c - 1, word, idx + 1, visited))
        if c + 1 < len(board[0]) and board[r][c + 1] == word[idx + 1]:
            result.append(self.exists_rec(board, r, c + 1, word, idx + 1, visited))
        visited[r][c] = False
        return any(result)

    def exist(self, board, word):
        visited = [[False] * len(board[0]) for x in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and self.exists_rec(board, r, c, word, 0, visited):
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "B", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    print(sol.exist(board, word))
