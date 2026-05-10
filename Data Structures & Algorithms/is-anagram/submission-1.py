class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Hash Table
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 # increment if in s
            count[ord(t[i]) - ord('a')] -= 1 # decremet if in t

        for val in count:
            if val != 0: # if 0: same number of letters
                return False
        return True
