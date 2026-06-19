class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) %2 == 1:
            return False
        collect = {'(': ')', '{':'}', '[':']'}
        stack = []
        for ch in s:
            if ch in collect:
                stack.append(ch)
            else:
                if stack and ch == collect[stack[-1]]:
                        stack.pop()
                
                else:
                    return False
        return len(stack) == 0

                



                

        