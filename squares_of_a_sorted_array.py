class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)):
            nums[x] *= nums[x]
        return sorted(nums)

    
#Binary Search Approach using two pointers (slower runtime but better solution, would be faster for large inputs)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = collections.deque()
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)
