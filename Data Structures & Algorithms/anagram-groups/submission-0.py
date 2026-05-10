class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        # Hash Table
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 # increment if in s
            count[ord(t[i]) - ord('a')] -= 1 # decrement if in t
        
        for val in count:
            if val != 0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        used = set()

        for i in range(len(strs)):
            if i in used:
                continue
            group = [strs[i]]
            used.add(i)
            for j in range(i+1, len(strs)):
                if self.isAnagram(strs[i], strs[j]):
                    group.append(strs[j])
                    used.add(j)
            result.append(group)
        
        return result
            

    
