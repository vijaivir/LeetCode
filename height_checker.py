class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for x in range(len(heights)):
            if heights[x] != expected[x]:
                count += 1
        return count
