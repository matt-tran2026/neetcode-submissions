class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_letters = {}
        t_letters = {}

        for letter in s:
            s_letters[letter] = s_letters.get(letter, 0) + 1

        for letter in t:
            t_letters[letter] = t_letters.get(letter,0) + 1

        if s_letters == t_letters:
            return True
        
        return False
        
        
