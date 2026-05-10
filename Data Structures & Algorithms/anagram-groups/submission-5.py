class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort - store by sorted string
        result = defaultdict(list)
        for s in strs: # sort each string
            sortedS = ''.join(sorted(s))
            result[sortedS].append(s) # store in same place with all other sortedS
        return list(result.values()) # convert dict to list
       