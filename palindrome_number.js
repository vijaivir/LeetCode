/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    if(x === reversedNum(x)){
        return true
    }
    return false
};

function reversedNum(num) {
  return (
    parseFloat(
      num
        .toString()
        .split('')
        .reverse()
        .join('')
    )
  )                 
};
