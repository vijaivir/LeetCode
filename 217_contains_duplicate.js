/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function(nums) {
    let un = [... new Set(nums)]
    if (un.length === nums.length){
        return false
    }
    return true
};