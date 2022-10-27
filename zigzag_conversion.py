class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = []
        for x in range(numRows):
            result.append([])
        direction = 0 
        ptr = 0
        for ch in s:
            if ptr == 0:
                result[ptr].append(ch)
                ptr += 1
                direction = 1
                continue
            if ptr == numRows - 1:
                result[numRows - 1].append(ch)
                ptr -= 1
                direction = 0
                continue
            if direction == 1:
                result[ptr].append(ch)
                ptr += 1
            else:
                result[ptr].append(ch)
                ptr -= 1
        final = ''
        for x in result:
            for c in x:
                final += c
        return final
