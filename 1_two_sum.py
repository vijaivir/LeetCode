class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [int] * 2
        for x in range(0, len(nums)):
            diff = target - nums[x]
            for i in range(x+1, len(nums)):
                if nums[i] == diff:
                    result[0] = x
                    result[1] = i
        return result