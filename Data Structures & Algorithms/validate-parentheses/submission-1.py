class Solution:
    def isValid(self, s: str) -> bool:
        # declare stack 
        # declare hashmap of close paren to open paren 
        # for char in s, if char in map, check if stack is filled and if the last added item in the stack 
        # is in map. If true, stack.pop, else return false 
        # if char not in map, append to stack 
        # if stack is empty return true, else return false 

        stack = []
        map = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in map:
                if stack and stack[-1] in map[char]:
                    stack.pop()
                else: 
                    return False
            if char not in map:
                stack.append(char)
        
        if not stack:
            return True
        else:
            return False