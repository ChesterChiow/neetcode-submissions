class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s # length#word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 

        while i < len(s):
            j = i
            while s[j] != '#': # find #
                j += 1
            length = int(s[i:j]) # find length
            i = j + 1 # start of word
            j = i + length # end of word
            res.append(s[i:j])
            i = j # move to next word
            
        return res
