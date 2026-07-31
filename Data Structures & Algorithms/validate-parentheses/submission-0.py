class Solution:
    def isValid(self, s: str) -> bool:
        #declare stack 
        #create hashmap which maps ')' to '('
        #iterate through each char in s 
        #if char is in hashmap, check if the stack is filled, 
        #and if the last value added to the stack is equal to a key in the hashmap, stack.pop if true 
        #else return false 
        #if the char is not in hashmap, append it to stack 
        #return true if stack is empty, else false 

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
        return False

      