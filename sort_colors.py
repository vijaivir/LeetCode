class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        count = collections.Counter(nums)
        for x in range(3):
            occurence = ptr + count[x]
            if occurence == 0:
                continue
            while ptr < occurence:
                nums[ptr] = x
                ptr += 1
