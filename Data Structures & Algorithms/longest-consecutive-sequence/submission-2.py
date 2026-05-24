class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # remove duplicate
        longest = 0

        for num in numSet:
            if (num-1) not in numSet: # choose the smallest number of the sequence
                length = 1 # start search
                while (num+length) in numSet: # find all the consecutive numbers
                    length += 1
                longest = max(length, longest) # store largest
        return longest
                