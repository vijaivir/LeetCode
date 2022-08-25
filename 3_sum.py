# O(n^3) Solution: Needs to be optimized!
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for x in range(len(nums)):
            i = nums[x]
            for y in range(len(nums)):
                if y != x:
                    j = nums[y]
                    for z in range(len(nums)):
                        if z != x and z != y:
                            k = nums[z]
                            sum = i + j + k
                            if sum == 0:
                                triplet = [i, j, k]
                                triplet.sort()
                                if triplet not in result:
                                    result.append(triplet)
        return result
