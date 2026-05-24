class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
 
        prefix = [0] * n # 0 0 0 0 
        suffix = [0] * n # 0 0 0 0 
        res = [0] * n    # 0 0 0 0 

        prefix[0] = 1   # 1 0 0 0
        suffix[n-1] = 1 # 0 0 0 1
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
            # 1  2  3  4  - nums
            # 1  1  2  6  - prefix

            # 1  2  3  4  - nums
            # 24 12 4  1  - suffix

            # 24 12 8 6

        return res
