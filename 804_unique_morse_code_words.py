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
