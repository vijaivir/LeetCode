# Credit: https://www.youtube.com/watch?v=s9fokUqJ76A
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesesStack = []
        result = []
        def recurse(openCount, closeCount):
            # Base Case
            if openCount == closeCount == n:
                result.append("".join(parenthesesStack))
                return
            if openCount < n:
                parenthesesStack.append("(")
                recurse(openCount + 1, closeCount)
                parenthesesStack.pop()
            if closeCount < openCount:
                parenthesesStack.append(")")
                recurse(openCount, closeCount + 1)
                parenthesesStack.pop()
        recurse(0, 0)
        return result