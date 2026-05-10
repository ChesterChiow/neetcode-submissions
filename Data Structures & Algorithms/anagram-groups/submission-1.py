class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort
        result = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            result[sortedS].append(s)
        return list(result.values()) # convert dict to list
       