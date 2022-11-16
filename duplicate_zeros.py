class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr) 
        i = 0
        j = len(arr)
        while i < j :
            if arr[i] == 0 :
                arr.insert(i+1 , 0)
                i += 1
            i += 1
        arr[:] = arr[:length]
