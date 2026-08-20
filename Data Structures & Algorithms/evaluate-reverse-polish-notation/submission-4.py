class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ele in tokens:
            if ele not in ['+', '-', '*', '/']:
                stack.append(int(ele))
            else:
                
                if ele == "+":
                    stack.append(stack.pop() + stack.pop())

                elif ele == "-":
                    first_pop = stack.pop()
                    second_pop = stack.pop()
                    stack.append(second_pop - first_pop)


                elif ele == "*":
                    stack.append(stack.pop() * stack.pop())

                else:
                    first_pop = stack.pop()
                    second_pop = stack.pop()
                    stack.append(int(float(second_pop) /first_pop))
        return stack[0]
        