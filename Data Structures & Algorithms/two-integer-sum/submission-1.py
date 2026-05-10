class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map
        prevMap = {} # value: indices

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []


