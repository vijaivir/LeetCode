class Solution:
    def maxArea(self, height: List[int]) -> int:
        lptr = 0
        rptr = len(height) - 1
        result = min(height[lptr], height[rptr]) * (rptr - lptr)
        while lptr != rptr:
            if height[lptr] < height[rptr]:
                lptr += 1
            else: 
                rptr -= 1
            if min(height[lptr], height[rptr]) * (rptr - lptr) > result:
                result = min(height[lptr], height[rptr]) * (rptr - lptr)
        return result
