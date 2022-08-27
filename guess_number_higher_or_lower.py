# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        # Binary division faster than (lowerBound + upperBound) //2
        my_guess = (low + high) >> 1
        # walrus operator ':=' - assigns value of the function to the variable 'res'
        # and then compare res with 0
        while (res := guess(my_guess)) != 0:
            if res == 1:
                low = my_guess + 1
            else:
                high = my_guess - 1
            my_guess = (low + high) >> 1

        return my_guess
