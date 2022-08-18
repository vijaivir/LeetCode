# This was my original approach but the "Time Limit Exceeded"
# It was imporved by using enumerate based on a discussion thread
# Credit: C0R3
# class Solution:
#     def minSetSize(self, arr: List[int]) -> int:
#         if len(arr) == 0:
#             return 0
#         size = len(arr)/2
#         result = []
#         for x in set(arr):
#             result.append(arr.count(x))
#         result.sort(reverse = True)
#         count = 0
#         total = 0
#         for x in result:
#             count += 1
#             total += x
#             if total >= size:
#                 return count

from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        size = len(arr)/2
        total = 0
        for i, count in enumerate(sorted(Counter(arr).values(), reverse = True)):
            total += count
            if total >= size:
                return i + 1
        return 0
