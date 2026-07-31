class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # declare stack 
        # for char in tokens 
        # if it is a arithmetic token, check what arithmetic is used and pop the last two numbers in the 
        # stack and perform that arithmetic. append that value to stack 
        # else push the numbers into stack
        # return stack[0]

        stack = []
        for char in tokens:
            if char == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            
            elif char == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)
            
            elif char == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))

            elif char == '/':
                c = int(stack.pop())
                d = (stack.pop())
                stack.append(int(d/c))
            
            else:
                stack.append(int(char))

        return stack[0]