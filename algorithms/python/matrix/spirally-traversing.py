# https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1

class Solution:

    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        traversal_list = []
        up_row, down_row, left_col, right_col = 0, r - 1, 0, c - 1
        while up_row <= down_row and left_col <= right_col:
            if up_row <= down_row:
                for i in range(left_col, right_col + 1):
                    traversal_list.append(matrix[up_row][i])
                up_row += 1
            if right_col >= left_col:
                for i in range(up_row, down_row + 1):
                    traversal_list.append(matrix[i][right_col])
                right_col -= 1
            if up_row <= down_row:
                for i in range(right_col, left_col - 1, -1):
                    traversal_list.append(matrix[down_row][i])
                down_row -= 1
            if right_col >= left_col:
                for i in range(down_row, up_row - 1, -1):
                    traversal_list.append(matrix[i][left_col])
                left_col += 1

        return traversal_list


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(values[k])
                k += 1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix, r, c)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends
