class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        count = [0] * 26 # [0,0,0,0,...]
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1 # increase count if in s
            count[ord(t[i])-ord('a')] -= 1 # decrease count if in t
    
        for val in count:
            if (val != 0):
                return False
        return True