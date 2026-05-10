class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set(nums) # set removes duplicates
        return len(hashSet) < len(nums)