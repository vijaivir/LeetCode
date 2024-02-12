class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = nums[0]
        for x in set(nums):
            if nums.count(x) > nums.count(result):
                result = x
        return result
