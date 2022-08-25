# ord() returns the Unicode value and 96 is subtracted to get
# the associated ASCII (97) to start indexing from 0 (i.e A=0, B=1 ...)
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = []
        for x in words:
            morsecode = ''
            for i in x:
                morsecode += morse[ord(i) - 97]
            result.append(morsecode)
        return len(set(result))
