class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        
        if len(nums) % 2 == 0:
            l = len(nums) // 2 - 1
            r = len(nums) // 2
            return (nums[l] + nums[r]) / 2
        else:
            return nums[(len(nums))//2]
