# https://leetcode.com/problems/flood-fill

from typing import List


class Solution:
    def fill(self, image: List[List[int]], sr: int, sc: int, newColor: int, currColor: int):
        if sr >= 0 and sr < len(image) and sc >= 0 and sc < len(image[0]) and image[sr][sc] == currColor:
            image[sr][sc] = newColor

            self.fill(image, sr + 1, sc, newColor, currColor)
            self.fill(image, sr - 1, sc, newColor, currColor)
            self.fill(image, sr, sc + 1, newColor, currColor)
            self.fill(image, sr, sc - 1, newColor, currColor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]:
            return image
        self.fill(image, sr, sc, newColor, image[sr][sc])
        return image
